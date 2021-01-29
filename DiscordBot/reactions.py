from discord.ext.commands import Cog
from discord import Client
from token_loader import CHANNEL_ID, MESSAGE_REACTION_ID, SERVER_ID
from helpers.reactions_helper import read_reactions_roles_from_file

class Reactions(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.client = Client()

    @Cog.listener()
    async def on_ready(self):
        self.reaction_message = await self.bot.get_channel(CHANNEL_ID).fetch_message(MESSAGE_REACTION_ID)
        self.reaction_roles = read_reactions_roles_from_file()


    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == self.reaction_message.id:
            current_roles = filter(lambda role: role in self.reaction_roles.values(), payload.member.roles)
            await payload.member.remove_roles(*current_roles)
            try:
                role = [role for role in payload.member.guild.roles if role.id == self.reaction_roles[payload.emoji.name]][0]
                await payload.member.add_roles(role)
                await self.reaction_message.remove_reaction(payload.emoji, payload.member)
            except KeyError:
                channel = self.bot.get_channel(CHANNEL_ID)
                await channel.send(f"{payload.member.name} nie wolno robić takich niecnych rzeczy! Reakcje może dodawać tylko admin.")


def setup(bot):
    bot.add_cog(Reactions(bot))