import discord
import time
from discord import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    while True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Progress: 90%"))
        time.sleep(10)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Progress: 90%"))
        time.sleep(10)

client.run('MTE5NzQxMTk1NjI0MDQxNjgxMA.Gwu2HV.mqTzS2Lwp5YTl6mQ1EVvYsksu1L7eCtzNP64ac')
