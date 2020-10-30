import discord
import youtube_dl
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.ext import tasks, commands
import datetime
import webbrowser
from random import randint
import asyncio
import time
import sys
import xmltodict
import urllib3
from bs4 import BeautifulSoup

class CurrencyCog(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.update()
       
    
    def update(self):
        self.x = Kurs()

    @commands.command()
    async def kurs(self,ctx, get_from, to, number):
        index_from = self.x.currency.index(get_from.upper())
        index_to = self.x.currency.index(to.upper())
        value_from = float(self.x.currency_value[index_from].replace(',','.'))
        value_to = float(self.x.currency_value[index_to].replace(',','.'))
        value = float(number.replace(',','.'))
        value = (value*value_from)/value_to
        await ctx.channel.send(str(value) + " " +self.x.currency[index_to])


class Kurs():
    def __init__(self):
        with open('kursy.xml', encoding="ISO-8859-2") as fd:
            self.doc = xmltodict.parse(fd.read()) 
            self.currency = []
            self.currency_value = []
            self.currency_multiplier = []
            self.read_name()
            self.read_value()
            self.read_multiplier()
            self.update()
    
    def update(self):
        http = urllib3.PoolManager()
        url = "https://www.nbp.pl/home.aspx?f=%2Fkursy%2Fkursya.html&fbclid=IwAR3Sir-RDL9hk0cvRcz7Jo2q3rTz1hbFwQgD6AReV0xeXrvj1JHQgV86s34"
        r = http.request('GET',url, preload_content=False)
        soup = BeautifulSoup(r.data)
        link = soup.find("p",{"class":"file print_hidden"}).find("a")
        nbp_site = "https://www.nbp.pl" + link.get('href')
        r.release_conn()
        print(nbp_site)
        r2 = http.request('GET',nbp_site, preload_content=False)
        with open('kursy.xml', 'wb') as out:
            out.write(r2.data)
        r2.release_conn()
    
    def read_name(self):
        self.currency.append("PLN")
        for i in self.doc["tabela_kursow"]["pozycja"]:
            self.currency.append(i.get('kod_waluty'))
        
    def read_value(self):
        self.currency_value.append("1,0")   
        for i in self.doc["tabela_kursow"]["pozycja"]:
            self.currency_value.append(i.get('kurs_sredni')) 
    
    def read_multiplier(self):
        self.currency_value.append("1")   
        for i in self.doc["tabela_kursow"]["pozycja"]:
            self.currency_value.append(i.get('przelicznik')) 


def setup(bot):
    bot.add_cog(CurrencyCog(bot))