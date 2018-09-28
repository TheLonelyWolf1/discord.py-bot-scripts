import os
import discord
import discord.ext
from discord.ext import commands
import datetime
import asyncio
import random
from random import randint
import time
import sys
import json

import Config
import SECRETS

bot = commands.Bot(command_prefix=Config.PREFIX, description=" ")
bot_version = Config.Version
players = {}


# ------------------------------
# On_Ready Output
# ------------------------------
# ------------------------------


@bot.event
async def on_ready():
    print("------------Eingeloggt--------------")
    print("Bot Name: " + bot.user.name)
    print("Bot ID: " + bot.user.id)
    print("Discord Version: " + discord.__version__)
    print("------------------------------------")


# ------------------------------
# Profile Status
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
async def profile(ctx, member: discord.Member = None):
    if member == None:
        author = ctx.message.author
        avatar = ctx.message.author.avatar_url
        joined = author.joined_at.__format__('%A, %d. %B %Y um %H:%M:%S')
        toprole = ctx.message.author.top_role
        nicker = ctx.message.author.nick
        userID = ctx.message.author.id
    else:
        author = member.name
        avatar = member.avatar_url
        joined = member.joined_at.__format__('%A, %d. %B %Y um %H:%M:%S')
        toprole = member.top_role
        nicker = member.nick
        userID = member.id
    embed = discord.Embed(title="User Information", color=discord.Color.dark_grey(),)
    embed.add_field(name="Username:", value=author)
    embed.set_thumbnail(url=avatar)
    embed.add_field(name='Nickname:', value=nicker, inline=True)
    embed.add_field(name='User ID:', value=userID, inline=False)
    embed.add_field(name="Höchste Role:", value=toprole, inline=False)
    embed.add_field(name='Beigetreten am:', value=joined, inline=False)
    await bot.say(embed=embed)


bot.run(token)
