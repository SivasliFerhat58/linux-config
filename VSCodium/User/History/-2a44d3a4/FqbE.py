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

client.run('token')
