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

epoch = datetime.datetime.utcfromtimestamp(0)

players = {}


# ------------------------------
# Responses
# ------------------------------
# ------------------------------


killResponses = ("%s ist aus Versehen in die Lave geschupst worden. UPS",
                 "%s ist auf ein Wolf gestoßen, danach hörte man nichts mehr von ihm.",
                 "Ich habe %s mal um die Ecke gebracht, kam alleine zurück.",
                 "Hat wer %s gesehen? War vorher mit ihm am Fluss.",
                 "Ich habe %s vergiftet. Wer möchte einen sterbenden %s sehen?",
                 "Habe %s 's Kopf weggerissen und in Mülleimer geworfen.",
                 "%s findet sein Gehirn nichtmehr. *Psst! Ich habs zerschrettert, sag es aber niemanden*",
                 "Sorry %s, aber ich musste dich leider erschießen.")


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
# Kill Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
async def kill(ctx, *, member: discord.Member = None):
    executor = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Kill-Command executed! By:', executor)
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Versuchte Mord von: ', member)
    if member is None:
        await bot.say("Wenn ich das Universum töte bleibt nichts mehr übrig und das möchte ich nicht!")
        return

    if member.id == "484382176180305950":
        await bot.say("Mich kann man nicht töten! Ich bin der Tod! :knife: ")
    elif member.id == "484382176180305950" and ctx.message.author.id == "261179915892686849":
        await bot.say("Ich möchte dich aber nicht töten, Meister!")
    elif member.id == "261179915892686849":
        await bot.say("Ich töte meinen Meister nicht!")
    elif member.id == ctx.message.author.id:
        await bot.say("Du kannst auch Selbstmord betreiben. Dann mach ich mir die Hände nicht schmutzig!")
    else:
        choice = killResponses[random.randrange(0, len(killResponses))] % member.mention
        await bot.say(choice)

bot.run(token)
