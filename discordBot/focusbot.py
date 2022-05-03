
from asyncio import tasks
from tkinter.tix import INTEGER

import pytz
from config import TOKEN
from config import canvasToken
from heapq import merge
import discord
from discord.ext import commands
from canvasapi import Canvas
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime, timezone
import datetime
from discord.ext import tasks

cred = credentials.Certificate("discordBot/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Canvas API URL
API_URL = "https://sit.instructure.com/"
# Canvas API key
API_KEY = canvasToken

canvas = Canvas(API_URL,API_KEY)

bot = commands.Bot(command_prefix="f-")

@bot.event
async def on_ready():
    print('we have logged in as {0.user}'.format(bot))


# update
@bot.command()

async def update(ctx):

        '''Updates the list of assignments from canvas'''

        await ctx.send("Updating in progress! Please do not use any commands until finished. (Note: This will take a minute :/ )")
        courses = canvas.get_courses(enrollment_state="active")

        for course in courses:
            assignments = course.get_assignments()
            '''cs is reference to the course from canvas'''
            cs = db.collection("{}".format(ctx.author)).document("courses").collection("courseName").document(course.name.replace("/"," "))
            if not(cs.get().exists):
                cs.set({course.name: True})
            '''loops though all assignments from canvas and input to firestore'''
            for assignment in assignments:
                result = db.collection("{}".format(ctx.author)).document("courses").collection(course.name.replace("/"," ")).document(assignment.name.replace("/"," "))
                if not(result.get().exists):
                    if assignment.due_at == None:
                        result.set({u"noDueDate":True, u"URL": assignment.html_url, u"Submissions": assignment.has_submitted_submissions} )
                    else:
                        dt = datetime.datetime.strptime(assignment.due_at, r'%Y-%m-%dT%H:%M:%SZ')
                        result.set({u"dueDate":dt, u"URL": assignment.html_url, u"Submissions": assignment.has_submitted_submissions} )
        

        db.collection("users").document("{}".format(ctx.author)).set({"{}".format(ctx.author): True})
        db.collection("{}".format(ctx.author)).document("day").set({u"setDay": 7})
                    
       
        await ctx.send("Updating complete!")


# get assignment - pull all assignments due in a week
@bot.command()
async def get_assignment(ctx):

    """List of all the asssignments due"""

    courses = db.collection("{}".format(ctx.author)).document("courses").collection("courseName").stream()
  
    for course in courses:
        embed=discord.Embed(title=course.id,inline=False)
        cnt = 1
        now= datetime.datetime.now()
        
        day = db.collection("{}".format(ctx.author)).document("day").get()
        day = day.to_dict()
        day = day["setDay"]
        docs = db.collection("{}".format(ctx.author)).document("courses").collection(course.id).where(u"dueDate", u">", now).where(u"dueDate", u"<", now+datetime.timedelta(days=day)).stream()
        '''for every assignment print all assignment'''
        for doc in docs:
            if cnt == 24:
                await ctx.send(embed = embed)
                embed=discord.Embed(title="Continued",inline=False)
                cnt = 0
            x = doc.to_dict()
        
            embed.add_field(name = doc.id,value = x["dueDate"],inline= False)
            '''if assignment was submited or not'''
            if x["Submissions"] == True:
                if "URL" in x:
                    embed.add_field(name = doc.id + " has been submitted",value = "url: "+ x["URL"],inline= False)
                else:
                    embed.add_field(name = doc.id + " has been submitted",value = "no url",inline= False)
            else:
                if "URL" in x:
                    embed.add_field(name = doc.id + " has not been submitted",value = "url: "+ x["URL"],inline= False)
                else:
                    embed.add_field(name = doc.id + " has not been submitted",value = "no url",inline= False)
            cnt += 1
        
        await ctx.send(embed = embed)   
    
    await ctx.send("List generated!")



# get all assignments due in the set range
"""@bot.command()
async def get_All_assignment(ctx):

    courses = db.collection("{}".format(ctx.author)).document("courses").collection("courseName").stream()
  
    for course in courses:
        embed=discord.Embed(title=course.id,inline=False)
        cnt = 1
        docs = db.collection("{}".format(ctx.author)).document("courses").collection(course.id).stream()
        
        for doc in docs:
            if cnt == 23:
                await ctx.send(embed = embed)
                embed=discord.Embed(title="Continued",inline=False)
                cnt = 0
            x = doc.to_dict()
            if "dueDate" in x:
                embed.add_field(name = doc.id,value = x["dueDate"],inline= False)
                cnt += 1
            if x["Submissions"] == True:
                if "URL" in x:
                    embed.add_field(name = doc.id + " has been submitted",value = "url: "+ x["URL"],inline= False)
                else:
                    embed.add_field(name = doc.id + " has been submitted",value = "no url",inline= False)
            else:
                if "URL" in x:
                    embed.add_field(name = doc.id + " has not been submitted",value = "url: "+ x["URL"],inline= False)
                else:
                    embed.add_field(name = doc.id + " has not been submitted",value = "no url",inline= False)
            cnt += 1
           
        await ctx.send(embed = embed)   
    
    await ctx.send("done")
"""


# clear - clear out all assignments
@bot.command()
async def clear(ctx):

    """Clears out all assignments + reupdates"""


    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["y", "n"]

    await ctx.send(f"This will delete all data (update is recommended after). Would you like to clear? (Y/N)")


    msg = await bot.wait_for("message")
    while not(check(msg)):
        ctx.send(f"Please input y or n: ")
        msg = await bot.wait_for("message")

    if msg.content.lower() == "n":
        await ctx.send("Clear command was aborted.")
        return
    
    await ctx.send("Clearing in progress! Please do not use any commands until finished. (Note: This will take a minute :/ )")
    
    courses = db.collection("{}".format(ctx.author)).document("courses").collection("courseName").stream()
    
    for course in courses:
        docs = db.collection("{}".format(ctx.author)).document("courses").collection(course.id).stream()
        
        for doc in docs:
            doc.reference.delete()
        
        course.reference.delete()
        
    datas = db.collection("{}".format(ctx.author)).stream()

    for data in datas:
        data.reference.delete()

    await ctx.send("Cleared!")



# get assignments for a specific course 
@bot.command()
async def get_course_assignment(ctx):

    """Get an assignment for a specific course"""

    def check(msg,ctx,sz):
        return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) > 0 and int(msg.content) < sz

    lst = []
    courses = db.collection("{}".format(ctx.author)).document("courses").collection("courseName").stream()

    embed=discord.Embed(title="Please select which course to see assignments from (enter a number >= 1) ",inline=False)
    arycnt = 1
    for course in courses:
        embed.add_field(name = course.id,value = arycnt,inline= False)
        lst.append(course.id)
        arycnt+=1
    
    await ctx.send(embed = embed) 

    msg = await bot.wait_for("message")
    while not(check(msg,ctx,arycnt)):
        await ctx.send(f"Please input a number greater than 0 and less than "+ arycnt)
        msg = await bot.wait_for("message")
        
    msg = int(msg.content)-1
    embed=discord.Embed(title=lst[msg],inline=False)
    
    cnt = 1
    now= datetime.datetime.now()
    day = db.collection("{}".format(ctx.author)).document("day").get()
    day = day.to_dict()
    day = day["setDay"]
    docs = db.collection("{}".format(ctx.author)).document("courses").collection(lst[msg]).where(u"dueDate", u">", now).where(u"dueDate", u"<", now+datetime.timedelta(days=day)).stream()
    for doc in docs:
        if cnt == 24:
            await ctx.send(embed = embed)
            embed=discord.Embed(title="Continued",inline=False)
            cnt = 0
        x = doc.to_dict()
        embed.add_field(name = doc.id,value = x["dueDate"],inline= False)
        cnt += 1
           
    await ctx.send(embed = embed) 

    await ctx.send("Here is your assignment!") 




# set assignment time range
@bot.command()
async def set_assignmentRange(ctx):
    
    """Sets time range for retreiving assignments"""

    def check(msg,ctx):
        return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) > 0 and int(msg.content) < 365
    
    embed=discord.Embed(title="Please input a number(days) greater than 0 and less than 365.",inline=False)
    await ctx.send(embed = embed) 
    msg = await bot.wait_for("message")
    while not(check(msg,ctx)):
        await ctx.send(f"Please input a number(days) greater than 0 and less than 365.")
        msg = await bot.wait_for("message")
        
    msg = int(msg.content)

    db.collection("{}".format(ctx.author)).document("day").set({u"setDay": msg})

    await ctx.send("Set Time Completed!") 



# add assignments not in canvas
@bot.command()
async def set_assignment(ctx):

    """Add an assignment not on canvas"""
    
    def check(message,ctx,sz):
        return message.author == ctx.author and message.channel == ctx.channel and int(message.content) > 0 and int(message.content) < sz

    courseList = []

    courses = db.collection("{}".format(ctx.author)).document("courses").collection("courseName").stream()
    embed=discord.Embed(title="Is this assignment related to one of your canvas courses?",inline=False)
    
    await ctx.send(embed = embed)
    message = await bot.wait_for("message")


    '''adding assignment to current course'''
    if message.content.lower()=="yes" or message.content.lower()== 'y':
        data={}
        assignmentName=""
        embed=discord.Embed(title="Which course?",inline=False)
        
    
        '''creates course list for user to pick from '''
        courseID = 1
        for course in courses:
            embed.add_field(name = course.id,value = courseID,inline= False)
            courseList.append(course.id)
            courseID+=1
        await ctx.send(embed = embed) 
        message = await bot.wait_for("message")

        '''checking if user selection is contained in given list'''
        while not(check(message,ctx,courseID)):
            await ctx.send(f"Try picking a number from the list! (1 to " + courseID +")")
            message = await bot.wait_for("message")

        '''setting course'''
        courseSelection=int(message.content)-1
        
        '''setting assignment name'''
        embed=discord.Embed(title="What should we call this assignment?",inline=False)
        await ctx.send(embed = embed)
        assignmentName=await bot.wait_for("message")
        
        ''' setting due date and submission status'''
        embed=discord.Embed(title="What is the due date in 'MM/DD/YYY hh:mm' format?",inline=False)
        await ctx.send(embed = embed)
        message = await bot.wait_for("message")
        dt = datetime.datetime.strptime(message.content, r'%m/%d/%Y %H:%M')
        data.update({u'dueDate':dt})
        data.update({u'Submissions': False})
        db.collection("{}".format(ctx.author)).document("courses").collection(courseList[courseSelection]).document(assignmentName.content).set(data)
        await ctx.send("Assignment added! :)")
        return
    
    
    '''adding assignment to course labeled 'other' for miscellaneous assignments'''
    if message.content.lower()=="no" or message.content.lower()== 'n' :
        data={}
        
        '''setting assignment name'''
        embed=discord.Embed(title="What should we call this assignment?",inline=False)
        await ctx.send(embed = embed)
        assignmentName= await bot.wait_for("message")
        
        ''' setting due date and submission status'''
        embed=discord.Embed(title="What is the due date in 'MM/DD/YYY hh:mm' format?",inline=False)
        await ctx.send(embed = embed)
        message = await bot.wait_for("message")
        dt = datetime.datetime.strptime(message.content, r'%m/%d/%Y %H:%M')
        data.update({u'dueDate':dt})
        data.update({u'Submissions': False})
        db.collection("{}".format(ctx.author)).document("courses").collection(u'other').document(assignmentName.content).set(data)
        db.collection("{}".format(ctx.author)).document("courses").collection(u'courseName').document(u"other").set({u'other': True})
        await ctx.send("Assignment added! :) *this one will be listed in 'other'*")
        return
    

@bot.command()
async def remind(ctx):

    """Reminders for assignments in canvas"""   

    courses = db.collection("{}".format(ctx.author)).document("courses").collection("courseName").stream()

    embed=discord.Embed(title="These are assignments set to be reminded: ",inline=False)
    await ctx.send(embed = embed) 

    for course in courses:
        
      
        now= datetime.datetime.now()
        
        day = db.collection("{}".format(ctx.author)).document("day").get()
        day = day.to_dict()
        day = day["setDay"]
        docs = db.collection("{}".format(ctx.author)).document("courses").collection(course.id).where(u"dueDate", u">", now).where(u"dueDate", u"<", now + datetime.timedelta(days=day)).stream()
        '''for every assignment print all assignment'''
        for doc in docs:
            x = doc.to_dict()
        
            if "dueDate" in x:
                
                
                '''if assignment was submited or not'''
                if x["Submissions"] == False:
                    
                    when = datetime.datetime.fromtimestamp(x["dueDate"].timestamp()) - datetime.timedelta(days=1)
                    
                    if now < when:
                        embed=discord.Embed(title=course.id,inline=False)
                        embed.add_field(name = doc.id,value = datetime.datetime.fromtimestamp(x["dueDate"].timestamp()),inline= False)
                        cs = db.collection("{}".format(ctx.author)).document("reminds").collection("remindName").document(doc.id)
                        if not(cs.get().exists):
                            cs.set({doc.id: True})
                        cs = db.collection("{}".format(ctx.author)).document("reminds").collection(doc.id).document(doc.id)
                        
                        if "URL" in x:
                            cs.set({'user_id': ctx.author.id, 'channel_id': ctx.channel.id, 'next_time': when, 'name': doc.id,"URL": x["URL"],'done': False})
                            embed.add_field(name = doc.id + " has not been submitted",value = "url: "+ x["URL"],inline= False)
                        else:
                            cs.set({'user_id': ctx.author.id, 'channel_id': ctx.channel.id, 'next_time': when, 'name': doc.id,'done': False})
                            embed.add_field(name = doc.id + " has not been submitted",value = "no url",inline= False)
           
                        await ctx.send(embed = embed) 

    await ctx.send("Reminders for Canvas Assignments above! Get working!") 



#set manual reminder
@bot.command()
async def set_reminder(ctx):

    '''Adding reminder to current course'''
    
    reminderName=""

    '''setting reminder name'''
    embed=discord.Embed(title="What should we call this reminder?",inline=False)
    await ctx.send(embed = embed)
    reminderName= await bot.wait_for("message")


    ''' setting due date and submission status'''
    embed=discord.Embed(title="What is the due date in 'MM/DD/YYYY hh:mm' format(Military time)?",inline=False)
    await ctx.send(embed = embed)
    msg = await bot.wait_for("message")

    """setting up url"""
    embed = discord.Embed(title="Do you have a url for the reminder? (Y/N)")
    await ctx.send(embed = embed)
    ans = await bot.wait_for("message")
    url = "None"

    if ans.content.lower() == "yes" or ans.content.lower() == "y":
        embed = discord.Embed(title="Please provide the URL: ")
        await ctx.send(embed = embed)
        url = await bot.wait_for("message")
        

    dt = datetime.datetime.strptime(msg.content, r'%m/%d/%Y %H:%M')
    cs = db.collection("{}".format(ctx.author)).document(u"reminds").collection(u"remindName").document(reminderName.content)
    if not(cs.get().exists):
        cs.set({reminderName.content: True})
    cs = db.collection("{}".format(ctx.author)).document(u"reminds").collection(reminderName.content).document(reminderName.content)
    if url == "None":
        cs.set({u'user_id': ctx.author.id, u'channel_id': ctx.channel.id, u'next_time': dt.astimezone(pytz.UTC), u'name': reminderName.content,'done': False,"manual": True})
    else:
        cs.set({u'user_id': ctx.author.id, u'channel_id': ctx.channel.id, u'next_time': dt.astimezone(pytz.UTC), u'name': reminderName.content,'done': False, u'URL': url.content,"manual": True})
    
    await ctx.send("Reminder added! :)")
    

@bot.command()
async def view_reminders(ctx):

    """View list of current reminders"""

    docs = db.collection("{}".format(ctx.author)).document(u"reminds").collection(u"remindName").stream()
    for doc in docs:
        ref = db.collection("{}".format(ctx.author)).document(u"reminds").collection(doc.id).document(doc.id).get()
        x = ref.to_dict()
        embed=discord.Embed(title=x["name"] ,inline=False)
        if "URL" in x:
            embed.add_field(name = "reminding at: " + str(datetime.datetime.fromtimestamp(x["next_time"].timestamp())),value = "url: "+ x["URL"],inline= False)
        else:
            embed.add_field(name = "reminding at: " + str(datetime.datetime.fromtimestamp(x["next_time"].timestamp())),value = "no url",inline= False)
        await ctx.send(embed = embed)
    await ctx.send("Reminders above! Hope it helps!")
        

@tasks.loop(seconds=5)
async def reminder():
    await bot.wait_until_ready()
    now = datetime.datetime.now()
    users = db.collection(u"users").stream()
    for user in users:
        docs = db.collection(user.id).document(u"reminds").collection(u"remindName").stream()

        for doc in docs:
            ref = db.collection(user.id).document(u"reminds").collection(doc.id).document(doc.id).get()
            x = ref.to_dict()
            if now > datetime.datetime.fromtimestamp(x["next_time"].timestamp()):
                embed=discord.Embed(title="reminder",inline=False)
                channel = bot.get_channel(x["channel_id"])
                if "URL" in x:
                    if "manual" in x:
                        embed.add_field(name = "Reminder for " + doc.id,value = "url: "+ x["URL"],inline= False)
                    else:
                        embed.add_field(name = doc.id + " is due in one day!",value = "url: "+ x["URL"],inline= False)
                else:
                    if "manual" in x:
                        embed.add_field(name = "Reminder for " + doc.id,value = "no url",inline= False)
                    else:
                        embed.add_field(name = doc.id + " is due in one day!",value = "no url",inline= False)
                    
                ref.reference.delete()
                refName = db.collection(user.id).document(u"reminds").collection(u"remindName").document(doc.id).get()
                refName.reference.delete()
                await channel.send(embed = embed)


@bot.command()
async def delete_reminders(ctx):
    docs = db.collection("{}".format(ctx.author)).document(u"reminds").collection(u"remindName").stream()
    for doc in docs:
        ref = db.collection("{}".format(ctx.author)).document(u"reminds").collection(doc.id).document(doc.id).get()
        x = ref.to_dict()
        embed=discord.Embed(title=x["name"] ,inline=False)
        if "URL" in x:
            embed.add_field(name = "reminding at: " + str(datetime.datetime.fromtimestamp(x["next_time"].timestamp())),value = "url: "+ x["URL"],inline= False)
        else:
            embed.add_field(name = "reminding at: " + str(datetime.datetime.fromtimestamp(x["next_time"].timestamp())),value = "no url",inline= False)
        
        ref.reference.delete()
        refName = db.collection("{}".format(ctx.author)).document(u"reminds").collection(u"remindName").document(doc.id).get()
        refName.reference.delete()
        await ctx.send(embed = embed)
    await ctx.send("Reminders deleted")
    
reminder.start()
bot.run(TOKEN,bot=True)
