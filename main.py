"""
main.py - minimal STANDALONE launcher for the boost card (only for a separate Railway service).

Use this ONLY if the boost feature runs as its own bot. If you already have your ELITE SYSTEM bot,
don't use this file: put boost_cog.py + boost_card.py + boost_bg.jpg in that bot's project instead
and add `await bot.load_extension("boost_cog")` in its setup_hook.

Railway variable needed:  DISCORD_TOKEN
"""
import os

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True   # enable "Message Content Intent" in the Discord developer portal
intents.members = True           # enable "Server Members Intent" too

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def setup_hook():
    await bot.load_extension("boost_cog")


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


bot.run(os.environ["DISCORD_TOKEN"])
