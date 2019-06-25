import discord
from discord.ext import commands

class Mycog:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def grosfdp(self):
        await self.bot.say("suertz :thumbsup: ")

def setup(bot):
    bot.add_cog(Mycog(bot))
