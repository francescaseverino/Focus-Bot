
from config import TOKEN
from heapq import merge
import discord
from discord.ext import commands
from canvasapi import Canvas
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Canvas API URL
API_URL = "https://sit.instructure.com/"
# Canvas API key
API_KEY = "Token"

canvas = Canvas(API_URL,API_KEY)

bot = commands.Bot(command_prefix="f-")

@bot.event
async def on_ready():
    print('we have logged in as {0.user}'.format(bot))


"""@bot.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    #bot does not answer it self
    if message.author == bot.user:
        return

    if message.channel.name == 'general':
        if user_message.lower() == "hello":
            response = f'hi'
            await message.channel.send(response)
            return"""




@bot.command()
async def update(ctx):
        courses = canvas.get_courses(enrollment_state="active")

        for course in courses:
            assignments = course.get_assignments()
           
            cs = db.collection("courses").document(course.name.replace("/"," "))
            if not(cs.get().exists):
                cs.set({course.name: True})
        
            for assignment in assignments:
                #if not(assignment.due_at is None or assignment.due_at == "null" or current_time > datetime.datetime.strptime(assignment.due_at, r'%Y-%m-%dT%H:%M:%SZ')):
                result = db.collection(course.name.replace("/"," ")).document(assignment.name.replace("/"," "))
                if not(result.get().exists):
                    if assignment.due_at == None:
                        result.set({u"noDueDate":True, u"URL": assignment.html_url, u"Submissions": assignment.has_submitted_submissions} )
                    else:
                        dt = datetime.datetime.strptime(assignment.due_at, r'%Y-%m-%dT%H:%M:%SZ')
                        result.set({u"dueDate":dt, u"URL": assignment.html_url, u"Submissions": assignment.has_submitted_submissions} )
                    
       
        await ctx.send("done")
        
@bot.command()
async def get_assignment(ctx):

    courses = db.collection("courses").stream()
  
    for course in courses:
        embed=discord.Embed(title=course.id,inline=False)
        cnt = 1
        n= datetime.datetime.now()
        docs = db.collection(course.id).where(u"dueDate", u">", n).where(u"dueDate", u"<", n+datetime.timedelta(days=7)).stream()
        
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


bot.run(TOKEN,bot=True)