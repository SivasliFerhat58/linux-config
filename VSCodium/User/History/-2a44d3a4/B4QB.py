import discord
import time

@client.event
async def on_ready():
    while True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Progress: 90%"))
        time.sleep(10)

