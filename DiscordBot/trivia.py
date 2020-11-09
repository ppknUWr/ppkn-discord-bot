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
import sys
import xmltodict
import urllib3
from bs4 import BeautifulSoup
import urllib.request, json 
import random
import re


class TriviaCog(commands.Cog):
    """
    Klasa wykonana przez Dominik Marcinkowski.
    Gra quiz na czacie discorda
    """
    def __init__(self,bot):
        """
        Konstruktor klasy
        """
        self.bot = bot
        self.trueanswer = ""
        self.answers = []
        self.questioned = False

    @commands.command()
    async def quiz(self,ctx):
        if(not self.questioned):
            await ctx.channel.send("Welcome to Quiz, type !quit to exit")
        self.clean()
        with urllib.request.urlopen("https://opentdb.com/api.php?amount=1") as url:
            data = json.loads(url.read().decode())
            
        self.trueanswer = data["results"][0]["correct_answer"]
        self.answers.append(self.trueanswer)
        self.answers += data["results"][0]["incorrect_answers"]
        random.shuffle(self.answers)
        self.question = data['results'][0]['question']
        
        # fixing incorrect character's encoding
        self.question = re.sub("&quot;", "\"", self.question)
        self.question = re.sub("&#039;", "\'", self.question)
        self.question = re.sub("&amp;", "&", self.question)
        
        await ctx.channel.send(self.question + "\n" + self.giveanswers())
        self.questioned = True
        
    
    def giveanswers(self):
        ch = 'a'
        x = ord(ch)
        res = ""
        for i in self.answers:
            res += chr(x) + ": " + i + "\n"
            x += 1
        return res

    def clean(self):
        self.trueanswer = ""
        self.answers = []
        self.questioned = False

    @commands.command()
    async def quit(self, ctx):
        if(self.questioned):
            await ctx.channel.send("Quiz has ended")
            self.clean()
    

    @commands.command()
    async def a(self,ctx):
        if(self.questioned):
            if(self.answers[0] == self.trueanswer):
                await ctx.channel.send("correct")
            else:
                await ctx.channel.send("incorrect, correct answer is " + self.trueanswer)
            await self.quiz(ctx)
    @commands.command()
    async def b(self,ctx):
        if(self.questioned):
            if(self.answers[1] == self.trueanswer):
                await ctx.channel.send("correct")
            else:
                await ctx.channel.send("incorrect, correct answer is " + self.trueanswer)
            await self.quiz(ctx)
    @commands.command()
    async def c(self,ctx):
        if(self.questioned):
            if(self.answers[2] == self.trueanswer):
                await ctx.channel.send("correct")
            else:
                await ctx.channel.send("incorrect, correct answer is " + self.trueanswer)
            await self.quiz(ctx)
    @commands.command()
    async def d(self,ctx):
        if(self.questioned):
            if(self.answers[3] == self.trueanswer):
                await ctx.channel.send("correct")
            else:
                await ctx.channel.send("incorrect, correct answer is " + self.trueanswer)
            await self.quiz(ctx)

def setup(bot):
    bot.add_cog(TriviaCog(bot))