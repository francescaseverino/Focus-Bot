
from tkinter.tix import INTEGER
from config import TOKEN
from config import canvasToken
from heapq import merge
import discord
from discord.ext import commands
from canvasapi import Canvas
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
import asyncio

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
        '''ctx is short for context which is the user who sent the command'''
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
        
        db.collection("{}".format(ctx.author)).document("day").set({u"setDay": 7})
                    
       
        await ctx.send("done")


# get assignment - pull all assignments due in a week
@bot.command()
async def get_assignment(ctx):

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
                embed.add_field(name = doc.id + " has been submitted",value = "url: "+ x["URL"],inline= False)
            else:
                embed.add_field(name = doc.id + " has not been submitted",value = "url: "+ x["URL"],inline= False)
            cnt += 1
        
        await ctx.send(embed = embed)   
    
    await ctx.send("done")



# get all assignments due in the set range
@bot.command()
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
                embed.add_field(name = doc.id + " has been submitted",value = "url: "+ x["URL"],inline= False)
            else:
                embed.add_field(name = doc.id + " has not been submitted",value = "url: "+ x["URL"],inline= False)
            cnt += 1
           
        await ctx.send(embed = embed)   
    
    await ctx.send("done")



# clear - clear out all assignments
@bot.command()
async def clear(ctx):
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["y", "n"]

    await ctx.send(f"This will delete all data(update is recommended after). Would you like to clear?(y or n)")


    msg = await bot.wait_for("message")
    while not(check(msg)):
        ctx.send(f"please input y or n")
        msg = await bot.wait_for("message")

    if msg.content.lower() == "n":
        await ctx.send("clear was aborted")
        return
    courses = db.collection("{}".format(ctx.author)).document("courses").collection("courseName").stream()
    
    for course in courses:
        docs = db.collection("{}".format(ctx.author)).document("courses").collection(course.id).stream()
        
        for doc in docs:
            doc.reference.delete()
        
        course.reference.delete()
        
    datas = db.collection("{}".format(ctx.author)).stream()

    for data in datas:
        data.reference.delete()

    await ctx.send("done")



# get assignments for a specific course 
@bot.command()
async def get_course_assignment(ctx):
    def check(msg,ctx,sz):
        '''what is sz?'''
        return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) > 0 and int(msg.content) < sz

    lst = []
    courses = db.collection("{}".format(ctx.author)).document("courses").collection("courseName").stream()

    embed=discord.Embed(title="Please select which course to see assignments from(enter a number >= 1)",inline=False)
    arycnt = 1
    for course in courses:
        embed.add_field(name = course.id,value = arycnt,inline= False)
        lst.append(course.id)
        arycnt+=1
    
    await ctx.send(embed = embed) 

    msg = await bot.wait_for("message")
    while not(check(msg,ctx,arycnt)):
        await ctx.send(f"please input a number greater than 0 and less than "+ arycnt)
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

    await ctx.send("done") 




# set assignment time range
@bot.command()
async def set_getAssignmentRange(ctx):
    
    def check(msg,ctx):
        return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) > 0 and int(msg.content) < 365
    
    embed=discord.Embed(title="please input a number(days) greater than 0 and less than 365",inline=False)
    await ctx.send(embed = embed) 
    msg = await bot.wait_for("message")
    while not(check(msg,ctx)):
        await ctx.send(f"please input a number(days) greater than 0 and less than 365")
        msg = await bot.wait_for("message")
        
    msg = int(msg.content)

    db.collection("{}".format(ctx.author)).document("day").set({u"setDay": msg})

    await ctx.send("done") 



bot.run(TOKEN,bot=True)
