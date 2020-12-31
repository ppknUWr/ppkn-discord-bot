import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
from discord import Client
import welcome_bot

"""
    Plik odpowiedzialny za konfiguracje bota i plikow zaleznych
"""
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

f = open('private/token.txt', 'r')
TOKEN = f.readline()
f.close


initialize_extensions = ['textchannelcommands'] # 'covid','kurswalut','trivia', voicechannelcommands
if __name__ == '__main__':
    for ext in initialize_extensions:
        bot.load_extension(ext)


def testing_function():
    return "Im a testing function!"


#signalize when ready to use
"""
    Inicjalizacja bota i podlaczenie go do serwera Discord
"""
@bot.event
async def on_member_join(member):
    await welcome_bot.welcome(member)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity = discord.Game(name = 'discord'))
bot.run(TOKEN, bot=True, reconnect=True)

