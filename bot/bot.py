#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by dragdev-studios


from discord.ext import commands
import sys
from bot import config


class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix=commands.when_mentioned_or(':gift:', '\U0001f381'), **kwargs)
        for cog in config.cogs:
            try:
                self.load_extension(cog)
            except Exception as exc:
                print('Could not load extension {0} due to {1.__class__.__name__}: {1}'.format(cog, exc))

    async def on_ready(self):
        print('Logged on as {0} (ID: {0.id})'.format(self.user))


bot = Bot()

@bot.event
async def on_connect():
    print(f"Connected to discord.")

@bot.event
def on_disconnect():
    print(f"Bot disconnected from discord!", file=sys.stderr)

# write general commands here

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

bot.run(config.token)
