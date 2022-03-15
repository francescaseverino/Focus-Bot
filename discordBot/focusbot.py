
from heapq import merge
import discord
import random
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
API_KEY = "1030~2u1bDNoJ2yBp0uTJdaYfxleZcagurrg0kUQ62NB71zL3ReUUhkhBVqYYkCfyf7U5"

canvas = Canvas(API_URL,API_KEY)


TOKEN = 'OTUzMDQzNDU0MDE4MDkzMDc2.Yi-04g.4NG8RXmB3KZ5nJq77ZDdNyyT8mQ'

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
async def who(ctx):
    await ctx.send("who askeeddddd")



@bot.command()
async def update(ctx):
        courses = canvas.get_courses(enrollment_state="active")

        for course in courses:
            assignments = course.get_assignments()
           
            current_time = datetime.datetime.now()
        
            for assignment in assignments:
                #if not(assignment.due_at is None or assignment.due_at == "null" or current_time > datetime.datetime.strptime(assignment.due_at, r'%Y-%m-%dT%H:%M:%SZ')):
                result = db.collection("{}".format(ctx.message.author)).document(course.name.replace("/"," ")).collection(assignment.name.replace("/"," ")).document("fields")
                if not(result.get().exists):
                    print(assignment.name)
                    result.set({"due date":assignment.due_at, "URL": assignment.html_url} )
       
        await ctx.send("done")

bot.run(TOKEN,bot=True)