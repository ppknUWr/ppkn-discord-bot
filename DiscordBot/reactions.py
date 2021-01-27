from discord.ext.commands import Cog
from token_loader import CHANNEL_ID, MESSAGE_REACTION_ID

class Reactions(Cog):

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        self.reaction_message = await self.bot.get_channel(CHANNEL_ID).fetch_message(MESSAGE_REACTION_ID)


def setup(bot):
    bot.add_cog(Reactions(bot))