import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.ext import tasks, commands
import datetime
import webbrowser
from random import randint
import asyncio
import time
import requests
import json

from helpers.stats_helper import count_how_long_is_member_playing
from token_loader import CHANNEL_ID, SERVER_ID, BOT_ID

base_url = "http://api.openweathermap.org/data/2.5/weather?"

class TextChannelCog(commands.Cog):
    """
    Komendy czatu tekstowego
    """
    def __init__(self, bot):
        self.bot = bot
        bot.loop.create_task(self.barka())
    
    def random_text(self, path):
        """
        Funkcja napisana przez Jakub Lorek.
        """
        try:
            with open(path, encoding="utf-8") as fp:
                text_array = []
                for text in fp:
                    text_array.append(text)
                return text_array[randint(0,len(text_array)-1)]
        except: FileNotFoundError

    async def sesja(self):
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(CHANNEL_ID)
        while not self.bot.is_closed():
            now = datetime.datetime.now()
            #                          year month day to countdown to
            future = datetime.datetime(2020, 6, 22)
            if(datetime.datetime.strftime(now,'%H:%M') == '16:00'):
                diff = future - now
                
                if(future.month < 10):
                    await channel.send(str(diff.days) + " dni do " + str(future.day) + '.0' + str(future.month) + '.' + str(future.year))
                else:
                    await channel.send(str(diff.days) + " dni do " + str(future.day) + '.' + str(future.month) + '.' + str(future.year))
                time = 86400
            else:
                time = 60
            await asyncio.sleep(time)

    async def barka(self): 
        """
        Funkcja napisana przez Kacper Malinowski.
        Funkcja wywolywana o danej godzinie o wiadomym przeznaczeniu
        """
        await self.bot.wait_until_ready()
        channel = self.bot.get_channel(CHANNEL_ID)
        while not self.bot.is_closed():
            now = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M')
            if now == '21:37':
                #code here
                await channel.send("@everyone 2137 https://i.imgur.com/L8pe8Ne.jpg")
                time = 86400
            else:
                time = 60
            await asyncio.sleep(time) 
    
    # @commands.command()
    # async def weather(self, ctx, arg):
    #     """
    #     Wyświetla aktualną pogodę w danym mieście
    #     Funkcja napisana przez Jakub Lorek.
    #     """
    #     city_name = arg
    #     complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    #     response = requests.get(complete_url)
    #     x = response.json()

    #     # checks if city name exists
    #     if x['cod'] != "404":
    #         y = x['main']
    #         current_temperature = round(y['temp'] - 273.15)
    #         current_pressure = y['pressure']
    #         current_humidity = y['humidity']
    #         z = x['weather']
    #         weather_description = z[0]['description']
    #         await ctx.send('Miasto: {0}\nTemperatura: {1}C\nCiśnienie: {2}hPa\nWilgotność: {3}%\nPogoda: {4}'.format(city_name, current_temperature, current_pressure, current_humidity, weather_description))
    #     else:
    #         await ctx.send("Miasto nie zostało znalezione, spróbuj ponownie")
    
    @commands.command()
    async def schapoinfo(self, ctx):
        """
        Wyświetla ciekawostki o narkotykach
        Funkcja napisana przez Jakub Lorek.
        """
        filepath = "./texts/drugsinfo.txt"
        string = self.random_text(filepath)
        await ctx.send(string)
   
    @commands.command()
    async def losowastrona(self, ctx):
        """
        Losuje artykuł na wikipedii
        Funkcja napisana przez Jakub Lorek.
        """
        await ctx.send("https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona")


    @commands.command()
    async def stats(self, ctx, arg = ""):
        server = self.bot.get_guild(int(SERVER_ID))
        member = [member for member in server.members if arg == member.name or member.mentioned_in(ctx.message)] # Getting the member [List]
        if member:
            member = member[0] # Because member is given in list [Object]

            if member.id != BOT_ID:
                if(member.status == discord.Status.online):

                    if(member.activities):
                        activity = member.activities[0]
                        start = datetime.datetime.timestamp(activity.start)
                        game_name = activity.name
                        await ctx.send(f"{member.name} gra teraz w {activity.name} i mogl przez ten czas skomplementowac {count_how_long_is_member_playing(start)}% tasków do BOTa.")

                    else:
                        await ctx.send(f"{member.name} nie zajmuje sie niczym, a moglby robic taski.")

                if(member.status == discord.Status.idle):
                    await ctx.send(f"{member.name} jest AFK.")

                if(member.status == discord.Status.dnd):
                    await ctx.send(f"{member.name} jest w trybie nie przeszkadzac, moze robi taski?")

                if(member.status == discord.Status.offline):
                    await ctx.send(f"{member.name} jest nieaktywny, twoje pingi tego nie zmienia")
                    
            else:
                await ctx.send("Jestem BOTem i w sumie to robie taski.")

        else:
            await ctx.send("Taki uzytkownik nie istnieje!")

    @commands.command()
    #admin only command
    @commands.has_permissions(administrator = True)
    async def delete(self,ctx):
        """
        Funkcja napisana przez Kacper Malinowski.
        Usuwa zadana ilosc wiadomości w kanale tekstowym.
        """
        number: int = 1
        
        temp = ctx.message.content[8:]
        try:
            number = int(temp)
        except:
            await ctx.message.channel.purge(limit = 1)
            await(await ctx.channel.send("Podaj cyfrę")).delete(delay = 2)
            return

        if(int(number) > 20):
            number = 20
        number = int(number)
        await ctx.channel.purge(limit = number + 1)
        if(number == 1):
            await(await ctx.channel.send("Wciągnięto " + str(number) + " kreskę! 👃👃👃")).delete(delay = 2)
        if(number > 1 and number < 5):
            await(await ctx.channel.send("Wciągnięto " + str(number) + " kreski! 👃👃👃")).delete(delay = 2)
        if(number >= 5):
            await(await ctx.channel.send("Wciągnięto " + str(number) + " kresek! 👃👃👃")).delete(delay = 2)

    @commands.command() #Funkcja stworzona do wyswietlania aktualnych danych na temat Covida
    async def covidSummary(self, ctx):
        r = requests.get('https://api.covid19api.com/summary')
        r = r.json()
        await ctx.send("Liczba nowych przypadków: " + str(r['Global']['NewConfirmed']) + "\n")
        await ctx.send("Liczba wszystkich przypadków: " + str(r['Global']['TotalConfirmed']) + "\n")
        await ctx.send("Liczba nowych zgonów: " + str(r['Global']['NewDeaths']) + "\n")
        await ctx.send("Liczba wszystkich zgonów: " + str(r['Global']['TotalDeaths']) + "\n")
        await ctx.send("Liczba nowych ozdrowieńców: " + str(r['Global']['NewRecovered']) + "\n")
        await ctx.send("Liczba wszystkich ozdrowieńców: " + str(r['Global']['TotalRecovered']) + "\n")


    @commands.command() #Funkcja stworzona do wyswietlania aktualnych danych na temat Covida dla podanego kraju
    async def covidCountry(self, ctx, arg):
        await ctx.send("Statystyki na temat COVID-19 dla kraju {} \n".format(arg))
        r = requests.get('https://api.covid19api.com/summary')
        r = r.json()
        for country in r['Countries']:
            if country["Country"] == arg:
                await ctx.send("Liczba nowych przypadków: " + str(country['NewConfirmed']) + "\n")
                await ctx.send("Liczba wszystkich przypadków: " + str(country['TotalConfirmed']) + "\n")
                await ctx.send("Liczba nowych zgonów: " + str(country['NewDeaths']) + "\n")
                await ctx.send("Liczba wszystkich zgonów: " + str(country['TotalDeaths']) + "\n")
                await ctx.send("Liczba nowych ozdrowieńców: " + str(country['NewRecovered']) + "\n")
                await ctx.send("Liczba wszystkich ozdrowieńców: " + str(country['TotalRecovered']) + "\n")

def setup(bot):
    bot.add_cog(TextChannelCog(bot))

