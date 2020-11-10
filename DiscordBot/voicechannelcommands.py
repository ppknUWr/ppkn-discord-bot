from __future__ import unicode_literals
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import os

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl' : 'music.mp3',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}
ffmpeg_options = {
    'options' : '-vn'
}

infobox = []

class YTDLSource(discord.PCMVolumeTransformer):
    """
    Klasa napisana przez Dominik Marcinkowski.
    Odpowiada za utworzenie strumienia audio miedzy Youtube a botem.
    """
    def __init__(self, source, *, data, volume = 0.5):
        super().__init__(source,volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')
    
    @classmethod
    async def from_url(cls,url,*, loop=None, stream=False):
        """
        Funkcja odpowiedzialna za zwrocenie strumienia do pliku w serwisie Youtube
        """
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda:ytdl.extract_info(url, download = not stream))

        if 'entries' in data:
            data = data['entries'][0]
        infobox.append(data['title'])
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class VoiceChannelCog(commands.Cog):
    """
    Klasa napisana przez Dominik Marcinkowski.
    Komendy czatu glosowego.
    """
    def __init__(self, bot): 
        self.bot = bot

    #channel control
    async def join(self,ctx):
        channel = ctx.message.author.voice.channel
        self.queues = []
        self.player = {}
        self.infoindex = 0
        
        await channel.connect()

    @commands.command()
    async def leave(self,ctx):
        self.queues = []
        self.player = {}
        infobox = []
        self.infoindex = 0
        await ctx.voice_client.disconnect()
    
    @commands.command()
    async def play(self, ctx, query):
        """
        Funkcja odpowiedzialna za odtwarzanie piosenki w kanale Discordowym.
        """
        if ctx.voice_client is None:
            await self.join(ctx)
        if ctx.voice_client.is_playing():
            self.queues.append(query)
            self.player[query] = await YTDLSource.from_url(query, loop=self.bot.loop, stream=True)
        else:
            self.queues.append(query)
            self.player[query] = await YTDLSource.from_url(query, loop=self.bot.loop, stream=True)
            self.next(ctx)
        print(self.queues)
        print(self.player)
        
    
    @commands.command()
    async def info(self, ctx):
        """
        Funkcja odpowiedzialna za wyswietlanie informacji o piosence w kanale Discordowym.
        """
        await ctx.channel.send("LECI NUTA: {}".format(self.queues[self.infoindex]))
        await ctx.channel.send("W kolejce : ")
        for i in range(self.infoindex + 1, len(self.queues)):
            await ctx.channel.send(str(i) + ". " + infobox[i])

    
    #same song more than 1 time doesn't work, self.player[query] is the problem
    def next(self,ctx,index = 0):
        """
        Funkcja odpowiedzialna za kolejkowanie piosenek.
        """
        #if index > 0:
        #    self.player.pop(self.queues[index - 1])
        #print(self.queues)
        #print(self.player)
        print(index)
        self.infoindex = index
        if (len(self.queues) > index):
            ctx.voice_client.play(self.player[self.queues[index]], after=lambda e: self.next(ctx, index = index + 1))  
        else:
            self.end_queue()
    
    def end_queue(self):
        self.queues = []
        self.player = {}
        infobox = []
        self.infoindex = 0
        print("done")

    @commands.command()
    async def pause(self,ctx):
        if(ctx.voice_client.is_playing()):
            ctx.voice_client.pause()
    
    @commands.command()
    async def resume(self,ctx):
        if(not ctx.voice_client.is_playing()):
            ctx.voice_client.resume()

def setup(bot):
    bot.add_cog(VoiceChannelCog(bot))