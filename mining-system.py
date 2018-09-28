
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

bot = commands.Bot(prefix="", description=" ")

@bot.event
async def on_ready():
    print("------------Logged in--------------")
    print("Bot Name: " + bot.user.name)
    print("Bot ID: " + bot.user.id)
    print("Discord Version: " + discord.__version__)
    print("------------------------------------")


# ------------------------------
# Delete Inventory's Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
async def deletestats(ctx,):
    id = ctx.message.author.id
    if id == "261179915892686849":
        f = open('users.json', 'w')
        f.write('{}')
        f.close()
        await bot.say("Roger! Sämtliche Inventare wurden **gelöscht**")
    else:
        await bot.say("Nope!")


# ------------------------------
# Inventory Join-Script
# ------------------------------
# ------------------------------


async def on_member_join(member):
    if os.path.isfile("users.json"):
        with open('users.json', 'r') as f:
            users = json.load(f)
        await update_data(users, member)
        with open('users.json', 'w') as f:
            json.dump(users, f)
    else:
        pass


# ------------------------------
# Data Updating-Script
# ------------------------------
# ------------------------------


async def update_data(users, user):
    if not user.id in users:
            users[user.id] = {}
            users[user.id]['stone'] = 0
            users[user.id]['kupfer'] = 0
            users[user.id]['eisen'] = 0
            users[user.id]['gold'] = 0
            users[user.id]['diamanten'] = 0
            users[user.id]['taler'] = 0
            users[user.id]['level'] = 1


# ------------------------------
# LevelUp-Script
# ------------------------------
# ------------------------------


async def level_up(users, user, channel):
    taler = users[user.id]['taler']
    lvl_start = users[user.id]['level']
    lvl_end = int(taler ** (1/4))
    if lvl_start < lvl_end:
        await bot.send_message(channel, '{} ist auf Level **{}** aufgestiegen!'.format(user.mention, lvl_end))
        users[user.id]['level'] = lvl_end


# ------------------------------
# Sell Command
# ------------------------------
# ------------------------------


stoneprize = Config.stoneprize
kupferprize = Config.kupferprize
eisenprize = Config.eisenprize
goldprize = Config.goldprize
diamandprize = Config.diamandprize


@bot.command(pass_context=True)
async def erzverkauf(ctx):
    embed = discord.Embed(description="Erz-Verkauf (*sell{Erz})",color=discord.Color.dark_grey(), )
    embed.add_field(name='Erz', value="WolfTaler pro Stück", inline=True)
    embed.add_field(name='Stein:', value=str(stoneprize), inline=True)
    embed.add_field(name='Kupfererz:', value=str(kupferprize), inline=True)
    embed.add_field(name='Eisenerz:', value=str(eisenprize), inline=True)
    embed.add_field(name='Golderz:', value=str(goldprize), inline=True)
    embed.add_field(name='Diamanten:', value=str(diamandprize), inline=True)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def sstein(ctx, count: str):
    userID = ctx.message.author.id
    if os.path.isfile("users.json"):
        with open('users.json', 'r') as f:
            users = json.load(f)
            stone = "{}".format(users[userID]['stone'])
            anzahl = int(count) * int(stoneprize)
            if stone < count:
                await bot.say("Du hast zuwenig Steine!")
            else:
                users[userID]['stone'] -= int(count)
                users[userID]['taler'] += anzahl
                await bot.say("Du hast {} Steine für {} WolfTaler verkauft!".format(count, anzahl))
        with open('users.json', 'w') as f:
            json.dump(users, f)

# ------------------------------


@bot.command(pass_context=True)
async def skupfer(ctx, count: str):
    userID = ctx.message.author.id
    if os.path.isfile("users.json"):
        with open('users.json', 'r') as f:
            users = json.load(f)
            stone = "{}".format(users[userID]['kupfer'])
            anzahl = int(count) * int(kupferprize)
            if stone < count:
                await bot.say("Du hast zuwenig Kupfer!")
            else:
                users[userID]['kupfer'] -= int(count)
                users[userID]['taler'] += anzahl
                await bot.say("Du hast {} Kupfererz für {} WolfTaler verkauft!".format(count, anzahl))
        with open('users.json', 'w') as f:
            json.dump(users, f)
# ------------------------------


@bot.command(pass_context=True)
async def seisen(ctx, count: str):
    userID = ctx.message.author.id
    if os.path.isfile("users.json"):
        with open('users.json', 'r') as f:
            users = json.load(f)
            stone = "{}".format(users[userID]['eisen'])
            anzahl = int(count) * int(eisenprize)
            if stone < count:
                await bot.say("Du hast zuwenig Eisenerz!")
            else:
                users[userID]['eisen'] -= int(count)
                users[userID]['taler'] += anzahl
                await bot.say("Du hast {} Eisenerz für {} WolfTaler verkauft!".format(count, anzahl))
        with open('users.json', 'w') as f:
            json.dump(users, f)
# ------------------------------


@bot.command(pass_context=True)
async def sgold(ctx, count: str):
    userID = ctx.message.author.id
    if os.path.isfile("users.json"):
        with open('users.json', 'r') as f:
            users = json.load(f)
            stone = "{}".format(users[userID]['gold'])
            anzahl = int(count) * int(goldprize)
            if stone < count:
                await bot.say("Du hast zuwenig Golderz!")
            else:
                users[userID]['gold'] -= int(count)
                users[userID]['taler'] += anzahl
                await bot.say("Du hast {} Golderz für {} WolfTaler verkauft!".format(count, anzahl))
        with open('users.json', 'w') as f:
            json.dump(users, f)
# ------------------------------


@bot.command(pass_context=True)
async def sdia(ctx, count: str):
    userID = ctx.message.author.id
    if os.path.isfile("users.json"):
        with open('users.json', 'r') as f:
            users = json.load(f)
            stone = "{}".format(users[userID]['diamanten'])
            anzahl = int(count) * int(diamandprize)
            if stone < count:
                await bot.say("Du hast zuwenig Diamanten!")
            else:
                users[userID]['diamanten'] -= int(count)
                users[userID]['taler'] += anzahl
                await bot.say("Du hast {} Diamanten für {} WolfTaler verkauft!".format(count, anzahl))
        with open('users.json', 'w') as f:
            json.dump(users, f)


# ------------------------------
# Stats Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
async def stats(ctx, member: discord.Member = None):
    if member is None:
        userID = ctx.message.author.id
    else:
        userID = member.id
    if os.path.isfile("users.json"):
        with open('users.json', 'r') as f:
            users = json.load(f)
            get_level = "{}".format(users[userID]['level'])
            wert = "{}".format(users[userID]['taler'])
            embed = discord.Embed(color=discord.Color.dark_grey(),)
            embed.add_field(name='WolfTaler:', value=wert, inline=True)
            embed.add_field(name='Level:', value=get_level, inline=True)
            await bot.say(embed=embed)
    else:
        return 0

# ------------------------------
# ErzInv Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
async def erzinv(ctx, member: discord.Member = None):
    if member is None:
        userID = ctx.message.author.id
    else:
        userID = member.id
    if os.path.isfile("users.json"):
        with open('users.json', 'r') as f:
            users = json.load(f)
            get_level = "{}".format(users[userID]['level'])
            stone = "{}".format(users[userID]['stone'])
            kupfer = "{}".format(users[userID]['kupfer'])
            eisen = "{}".format(users[userID]['eisen'])
            gold = "{}".format(users[userID]['gold'])
            dias = "{}".format(users[userID]['diamanten'])
            wert = "{}".format(users[userID]['taler'])
            embed = discord.Embed(description="Erz Inventar",color=discord.Color.dark_grey(),)
            embed.add_field(name='Steine:', value=stone, inline=True)
            embed.add_field(name="Kupfererze:", value=kupfer, inline=True)
            embed.add_field(name='Eisenerze:', value=eisen, inline=True)
            embed.add_field(name='Golderze:', value=gold, inline=True)
            embed.add_field(name='Diamanten:', value=dias, inline=True)
            await bot.say(embed=embed)
    else:
        return 0


# ------------------------------
# Mine Command
# ------------------------------
# ------------------------------


@bot.command(pass_context=True)
@commands.cooldown(1, Config.Cooldown, commands.BucketType.user)
async def mine(ctx):
    message = ctx.message
    user = ctx.message.author
    if os.path.isfile("users.json"):
        with open('users.json', 'r') as f:
            users = json.load(f)
        await update_data(users, message.author)

        dias = randint(1, 5)
        users[user.id]['diamanten'] += dias
        stone = randint(6, 14)
        users[user.id]['stone'] += stone
        kupfer = randint(4, 11)
        users[user.id]['kupfer'] += kupfer
        eisen = randint(3, 9)
        users[user.id]['eisen'] += eisen
        gold = randint(2, 7)
        users[user.id]['gold'] += gold
        await level_up(users, message.author, message.channel)
        with open('users.json', 'w') as f:
            json.dump(users, f)
        embed = discord.Embed(description="Deine Ausbeute:", color=discord.Color.dark_grey(),)
        embed.add_field(name='Steine:', value=stone, inline=True)
        embed.add_field(name="Kupfererze:", value=kupfer, inline=True)
        embed.add_field(name='Eisenerze:', value=eisen, inline=True)
        embed.add_field(name='Golderze:', value=gold, inline=True)
        embed.add_field(name='Diamanten:', value=dias, inline=True)
        await bot.say(embed=embed)
    else:
        return
   

bot.run(token)
