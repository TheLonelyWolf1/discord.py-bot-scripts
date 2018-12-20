@bot.command(pass_context=True)
async def deleteribbons(ctx,):
    id = ctx.message.author.id
    if id == "261179915892686849":
        f = open('users.json', 'w')
        f.write('{}')
        f.close()
        await bot.say("Roger! All Ribbons from all Players are **deleted**")
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
            users[user.id]['moh'] = 0
            users[user.id]['sstar'] = 0


@bot.command(pass_context=True)
async def addribbon_moh(ctx, member : discord.Member = None):
    message = ctx.message
    user = member
    if member is None:
        await bot.say("No User specified!")
    else:
        userID = member.id
        if os.path.isfile("users.json"):
            with open('users.json', 'r') as f:
                users = json.load(f)
            await update_data(users, message.author)
            users[user.id]['moh'] += 1
            with open('users.json', 'w') as f:
                json.dump(users, f)
            await bot.say("Ribbon added!")
        else:
            return 0


@bot.command(pass_context=True)
async def addribbon_silverstar(ctx, member : discord.Member = None):
    message = ctx.message
    user = member
    if member is None:
        await bot.say("No User specified!")
    else:
        userID = member.id
        if os.path.isfile("users.json"):
            with open('users.json', 'r') as f:
                users = json.load(f)
            await update_data(users, message.author)
            users[user.id]['sstar'] += 1
            with open('users.json', 'w') as f:
                json.dump(users, f)
            await bot.say("Ribbon added!")
        else:
            return 0

#----------------------------------------------------------
# DELETE RIBBONS
@bot.command(pass_context=True)
async def delribbon_moh(ctx, member : discord.Member = None):
    message = ctx.message
    user = member
    if member is None:
        await bot.say("No User specified!")
    else:
        userID = member.id
        if os.path.isfile("users.json"):
            with open('users.json', 'r') as f:
                users = json.load(f)
            await update_data(users, message.author)
            users[user.id]['moh'] -= 1
            with open('users.json', 'w') as f:
                json.dump(users, f)
            await bot.say("Ribbon removed!")
        else:
            return 0


@bot.command(pass_context=True)
async def delribbon_silverstar(ctx, member : discord.Member = None):
    message = ctx.message
    user = member
    if member is None:
        await bot.say("No User specified!")
    else:
        userID = member.id
        if os.path.isfile("users.json"):
            with open('users.json', 'r') as f:
                users = json.load(f)
            await update_data(users, message.author)
            users[user.id]['sstar'] -= 1
            with open('users.json', 'w') as f:
                json.dump(users, f)
            await bot.say("Ribbon removed!")
        else:
            return 0
#----------------------------------------------
#Myribbons

@bot.command(pass_context=True)
async def myribbons(ctx, member: discord.Member = None):
    if member is None:
        userID = ctx.message.author.id
    else:
        userID = member.id
    if os.path.isfile("users.json"):
        with open('users.json', 'r') as f:
            users = json.load(f)
            ribbon1 = "{}".format(users[userID]['moh'])
            ribbon2 = "{}".format(users[userID]['sstar'])
            if ribbon1 is None:
                ribbon1 = 0
            else:
                ribbon1 = ribbon1
            if ribbon2 is None:
                ribbon2 = 0
            else:
                ribbon2 = ribbon2
            embed = discord.Embed(description="My Ribbons", color=discord.Color.dark_grey(),)
            embed.add_field(name='Medal of Honor', value=ribbon1, inline=True)
            embed.add_field(name='Silver Star', value=ribbon2, inline=True)
            await bot.say(embed=embed)
    else:
        return 0
