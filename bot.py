import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import asyncio
startup_extensions = ["Music"]
bot = commands.Bot("?")

@bot.event
async def on_ready():

    print("Bot online")

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong")
@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("Salutari!Cfr e viata si MUIE U")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(e.__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
bot.run("Mzg4ODA2MzI0NjY3ODA5Nzkz.DQyXxQ.jQJZzkkp-eBccK6kkHO1bWu_igc")
