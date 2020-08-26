from discord.ext import commands

class main:
    def __init__(self, bot):
        self.bot = bot
    
    @bot.command()
    async def info(ctx):
        pass

    @bot.command()
    async def about(ctx):
        pass

    @bot.command()
    async def invite(ctx):
        await ctx.send(f"**Invite me to your server!** \n[link]")

    @bot.command()
    async def ping(ctx):
        await ctx.send(f":ping_pong: Pong! `{bot.latency*1000}ms`")

def setup(bot):
    bot.add_cog(MainCog(bot))