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



send_time = '21:37'
f = open('private/channel.txt','r')

message_channel_id = int(f.readline())

f.close()

f = open('private/server.txt','r')

server_id = int(f.readline())

f.close()

# f = open('private/weatherapi.txt','r')

# api_key = f.readline()

# f.close()

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
        channel = self.bot.get_channel(message_channel_id)
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
        channel = self.bot.get_channel(message_channel_id)
        while not self.bot.is_closed():
            now = datetime.datetime.strftime(datetime.datetime.now(),'%H:%M')
            if now == send_time:
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

    """
    TODO: Bugfix - komenda stats wywolana na bocie powoduje error
    TODO: Refraktoryzacja kodu
    """
    @commands.command(aliases=['adam'])
    async def stats(self, ctx, arg = "Pandamonium"):
        #Getting Adam member
        server = self.bot.get_guild(int(server_id))
        member = [member for member in server.members if arg == member.name or member.mentioned_in(ctx.message)]
        if member:
            member = member[0]
            if(member.status == discord.Status.online):
                if(member.activities):
                    await ctx.send("Member ma jakas aktywnosc :)")
                else:
                    await ctx.send("Member nie ma aktywnosci :(")

            if(member.status == discord.Status.idle):
                await ctx.send("Member jest AFK, moze poszedl cos przekasic :D")

            if(member.status == discord.Status.dnd):
                await ctx.send("Member ma tryb nie przeszkadzac wiec przestan go pingowac")

            if(member.status == discord.Status.offline):
                await ctx.send("Member jest nieaktywny, twoje pingi tego nie zmienia")
        else:
            await ctx.send("Taki uzytkownik nie istnieje!")
        # for member in server.members:
        #     if (arg == member.name or member.mentioned_in(ctx.message)):
        #         print(member)
        # print(member)
        # for member in server.members:
        #     if(member.status == discord.Status.online):
        #         print(member.activities)
        #     if (arg == member.name or member.mentioned_in(ctx.message)):
        #         if(member.status == discord.Status.online!):
        #             if(str(member.activities) == "()" or str(member.activities[0]) == "None"):
        #                 await ctx.send("{0} nic nie robi".format(member.name))
        #                 break
        #             for activity in member.activities:
        #                 if (activity.type == discord.ActivityType.playing):
        #                     game_name = activity.name

        #                     #Counting how long member is playing
        #                     timestamp = activity.timestamps
        #                     start = timestamp["start"]
        #                     now = int(round(time.time() * 1000))
        #                     diff = now - start
        #                     time_delta = datetime.timedelta(milliseconds=diff)
        #                     final_time = str(time_delta).split(".")[0]

        #                     #Counting how much money member would gain
        #                     minimal_wage = 0.000472      # PLN per milliseconds
        #                     income = round((diff * minimal_wage)/100) 
        #                     await ctx.send("{0} marnował życie w {1} przez {2}, mógł zarobić przez ten czas {3} PLN".format(member.name, game_name, final_time, income))
        #                     break
        #                 if (activity.type == discord.ActivityType.listening):
        #                     #Counting how long member is listening
        #                     start = activity.created_at
        #                     start = start.timestamp() * 1000 + 3600000 * 2
        #                     now = int(round(time.time() * 1000))
        #                     diff = now - int(start)
        #                     time_delta = datetime.timedelta(milliseconds=diff)
        #                     final_time = str(time_delta).split(".")[0]

        #                     #Counting how much money member would gain
        #                     minimal_wage = 0.000472      # PLN per milliseconds
        #                     income = round((diff * minimal_wage)/100) 
        #                     await ctx.send("{0} słucha jakiejś dobrej nuty już przez {1}, zająłby się czymś pożytecznym, {2} PLN piechotą nie chodzi".format(member.name, final_time, income))
        #                     break
        #         elif(member.status == discord.Status.idle):
        #             await ctx.send("{0} poszedł afk albo coś".format(member.name))
        #         elif(member.status == discord.Status.dnd):
        #             await ctx.send("{0} zasnął przed biurkiem jak nic".format(member.name))
        #         if(member.status == discord.Status.offline):
        #             await ctx.send("{0} śpi albo nie żyje inaczej by grał".format(member.name))

    
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

