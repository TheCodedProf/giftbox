from discord.ext import commands

class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.group()
    async def giveaway(self,ctx):
        '''Controls a giveaway'''
        await ctx.send("Invalid command passed. Use `giveaway add` to start a giveaaway.")

    @giveaway.command()
    async def add(self, ctx):
        '''Adds a giveaway'''
        pass

    @giveaway.command()
    async def remove(self, ctx):
        '''Removes a giveaway'''
        pass

def setup(bot):
    bot.add_cog(main(bot))