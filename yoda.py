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
players = {}


# ------------------------------
# Responses
# ------------------------------
# ------------------------------

yodaResponses = ("Schlafen du jetzt musst, sonst du morgen müde sein wirst.",
                 "Unmöglich zu sehen, die Zukunft ist.",
                 "Groß machen Kriege niemand.",
                 "Furcht der Pfad zur dunklen Seite ist.",
                 "Eure Sinne ihr nutzen müsst.",
                 "Die Macht stark in dir ist.",
                 "Grammatik ich von Yoda gelernt haben.",
                 "Viel zu lernen du noch hast, mein junger Padawan.",
                 "Tue es oder tue es nicht! Versuchen es nicht gibt.",
                 "Die macht nur zur Verteidigung benutzen du darfst. Niemals zum Angriff!",
                 "Dich lebend zu sehen mich erfreut, %s",
                 "Der Tod ein natürlicher Bestandteil des Lebens ist.",
                 "Ins Exil ich muss, versagt ich haben.",
                 "Feigling du bist, wenn du folgen der dunklen Seite.",
                 "Kleine Truppe wir sind, dafür größer im Geist.",
                 "Deine Wahrnehmung deine Realität bestimmen wird.",
                 "Geburtstag du hast! Alter Sack du jetzt bist.",
                 "Müde ich bin, Kaffee ich jetzt brauch.",
                 "Montag! Schrecklich er ist.",
                 "Schnauze halten du musst, bis ich Kaffee fertig getrunken habe.",
                 "Möge das Wetter mit deuch sein.",
                 "Yodafone - Der Internetanbieter für Jedis",
                 "Kaffee du bringen mir musst, sonst töten ich dich werde.",
                 "Die dunkle Seite stärker als Chuck Norris ist.",
                 "Auf dein Herz hören du musst, um zu erfüllen deine Träume.",
                 "Du nicht grundlos töten darfst!")


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
# Yoda Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
async def yoda(ctx, *, member: discord.Member = None):
    executor = ctx.message.author
    print(datetime.datetime.now().strftime("[%d-%m-%y|%H:%M:%S]"), 'Yoda-Command executed! By:', executor)
    choice = yodaResponses[random.randrange(0, len(yodaResponses))]
    await bot.say(embed=discord.Embed(color=discord.Color.dark_green(), description=choice))



bot.run(token)
