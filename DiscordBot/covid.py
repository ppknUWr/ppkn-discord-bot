import discord
import youtube_dl
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.ext import tasks, commands
import COVID19Py
import pprint
import asyncio
import time

covid19 = COVID19Py.COVID19(data_source = "jhu")

def removekey(d,key):
    r = dict(d)
    del(r[key])
    return r

class CovidCog(commands.Cog):
    """
    Klasa wykonana przez Kacper Malinowski.
    Wyswietla biezacy status liczby zachorowan na COVID-19, aktualizowany co godzine
    """
    def __init__(self,bot):
        """
        Konstruktor klasy
        """
        self.bot = bot
        bot.loop.create_task(self.get_latest())
        bot.loop.create_task(self.get_all())
   
    async def get_latest(self):
        """
        Pobiera ogolna wartosc zachorowan na swiecie.
        """
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            latest_cases_file = open("covid/latest_cases.txt","w")
            latest = covid19.getLatest()
            latest = removekey(latest,'recovered')
            pprint.pprint(latest,latest_cases_file)
            latest_cases_file.close()
            await asyncio.sleep(3600)
   
    async def get_all(self):
        """
        Pobiera dane dotyczace zachorowan z kazdego kraju.
        """
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            location_cases_file = open("covid/location_cases.txt","w")
            locations = covid19.getLocations(rank_by = 'confirmed')

            final_dict = []
            for x in range(len(locations)):
                temp = locations[x]
                #comment lines to save coresponding attributes to file
                temp = removekey(temp,'coordinates')                                        #dictionary {latitude : float, longitude : float}
                #temp = removekey(temp,'country')                                           #str
                #temp = removekey(temp,'country_code')                                      #str
                temp = removekey(temp,'country_population')                                 #int
                temp = removekey(temp,'id')                                                 #int
                temp = removekey(temp,'last_updated')                                       #time e.g. '2020-05-07T13:11:16.160361Z'
                #temp = removekey(temp,'latest')                                            #dictionary {confirmed : int, deaths : int, recovered : int}    recovered for some reason is always 0
                temp = removekey(temp,'province')                                           #str
                final_dict.append(temp)
            locations = final_dict
            pprint.pprint(locations,location_cases_file)
            location_cases_file.close()
            await asyncio.sleep(3600)
    
    @commands.command()
    async def world(self,ctx,context: str = ''):
        """
        Wyswietla ilosc zachorowan na swiecie.
        """
        latest_cases_file = open("covid/latest_cases.txt","r")
        #get data from file as dictionary
        latest_cases = eval(latest_cases_file.read())

        message = "Kornonaświrus raport:\n"
        if(context == 'confirmed'):
            message += str("confirmed: " + str(latest_cases['confirmed']))
        elif(context == 'deaths'):
             message += str("confirmed: " + str(latest_cases['deaths']))
        else:
             message += str("confirmed: " + str(latest_cases['confirmed']) + "\ndeaths: " + str(latest_cases['deaths']))
        await ctx.channel.send(message)
   
    @commands.command()
    async def all(self,ctx):
        """
        Wyswietla ilosc zachorowan z top 10 krajow
        """
        context = None
        default_limit = 10
        temp = ctx.message.content[5:]
        try:
            context = int(temp)
            if context > default_limit:
                context = default_limit
        except:
            context = str(temp)

        location_cases_file = open("covid/location_cases.txt","r")
        #get data from file as dictionary
        location_cases = eval(location_cases_file.read())
        message = "Kornonaświrus raport:\n"

        wanted_dictionary = {}

        #display x amount of countries and thier cases from highest to lowest, default is 10, for now it's hardcoded for countries confirmed cases and deaths
        if type(context) == int:
            for i in range(context):
                message += str(str(i+1) + ". " + str(location_cases[i]['country']) + " \tconfirmed: " + str(location_cases[i]['latest']['confirmed'])  + " \tdeaths: " + str(location_cases[i]['latest']['deaths'])+ "\n")
            await ctx.channel.send(message) 

        elif type(context) == str and len(context) != 0:
            found = False
            for i in range(len(location_cases)):
                temp = location_cases[i]
                if context in temp.values():
                    wanted_dictionary = temp
                    found = True
                    break
            if found == True:
                message += str(wanted_dictionary['country'] + "\tconfirmed: " + str(wanted_dictionary['latest']['confirmed']) + "\tdeaths: " + str(wanted_dictionary['latest']['deaths']))
                await ctx.channel.send(message)
            elif found == False:
                await ctx.channel.send("Nie znaleziono takiego kraju!")

        elif type(context) == str and len(context) == 0:
            for i in range(default_limit):
                message += str(str(i+1) + ". " + str(location_cases[i]['country']) + " \tconfirmed: " + str(location_cases[i]['latest']['confirmed'])  + " \tdeaths: " + str(location_cases[i]['latest']['deaths'])+ "\n")
            await ctx.channel.send(message) 



def setup(bot):
    bot.add_cog(CovidCog(bot))