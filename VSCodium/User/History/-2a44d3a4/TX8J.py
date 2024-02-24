import discord
import time
from discord.ext import commands, tasks
import asyncio


intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

activities = [" |--· · · · · · · · | ",""]

@tasks.loop(seconds=2)
async def change_activity():
    activity = discord.Game(name=activities[0])  # İlk aktiviteyi al
    await client.change_presence(activity=activity)
    activities.append(activities.pop(0))

@client.event
async def on_ready():
    change_activity.start()


client.run('')
