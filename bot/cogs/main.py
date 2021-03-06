from discord.ext import commands

class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def info(self,ctx):
        '''Shows info about the bot'''
        pass

    @commands.command()
    async def about(self,ctx):
        '''Shows how this Giftbox works'''
        pass

    @commands.command()
    async def invite(self,ctx):
        '''Invite me to your server!'''
        await ctx.send(f"**Invite me to your server!** \n[link]")

    @commands.command()
    async def ping(self,ctx):
        '''Tests the latency of the bot'''
        await ctx.send(f":ping_pong: Pong! `{self.bot.latency*1000}ms`")

def setup(bot):
    bot.add_cog(main(bot))