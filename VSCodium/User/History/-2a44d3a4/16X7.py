import discord
import time
from discord.ext import commands, tasks
import asyncio


intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

activities = ["Progress: 90%","Az Daha Sabır Bitti Sayılır","Botu Kullanmaya Çalışmayın"]

@tasks.loop(seconds=2)
async def change_activity():
    activity = discord.Game(name=activities[0])  # İlk aktiviteyi al
    await bot.change_presence(activity=activity)
    activities.append(activities.pop(0))

@client.event
async def on_ready():
    while True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Progress: 90%"))
        time.sleep(10)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Progress: 90%"))
        time.sleep(10)

client.run('MTE5NzQxMTk1NjI0MDQxNjgxMA.Gwu2HV.mqTzS2Lwp5YTl6mQ1EVvYsksu1L7eCtzNP64ac')
