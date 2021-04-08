import discord
import json
import random
import os

from os import path
from discord.ext import commands

Keys = {}

intents = discord.Intents().all()
client = commands.Bot(command_prefix='!', intents=intents)
#currentGuild = discord.Guild

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #readFileJson("users.json", usersData)
    #print(str(currentGuild))
"""
@client.event
async def on_message(ctx):
    if ctx.author == client.user:
        return

    if ctx.content.startswith('!') == False:
        if ctx.content.find("hello") != -1:
            await ctx.channel.send('Hello!')
    await client.process_commands(ctx)
"""
@client.command()
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommmandNotFound):
		await ctx.send('Invalid command')

#COMMAND: hello, will respond with 'world' 
@client.command()
async def hello(ctx):
    """Send text message 'world'"""
    await ctx.send("world")
    return

#COMMAND: happy, will respond with the slight_smile emoji
@client.command()
async def happy(ctx):
    """Send :slight_smile: Emoji"""
    await ctx.send(":slight_smile:")
    return

#COMMAND: dice, will send value found by random generation
@client.command()
async def dice(ctx, arg):
    """Roll Dice(.dice help to see options"""
    dice_result=0
    if arg == "help":
        await ctx.send("!dice <dicetype>")
        await ctx.send("dicetype: d4, d6, d8, d10, d12, d20")
        return
    #d4 roll
    if arg == "d4":
        dice_result = random.randint(1,4)
    #d6 roll
    if arg == "d6":
        dice_result = random.randint(1,6)
    #d8 roll
    if arg == "d8":
        dice_result = random.randint(1,8)
    #d10 roll
    if arg == "d10":
        dice_result = random.randint(1,10)
    #d12 roll
    if arg == "d12":
        dice_result = random.randint(1,12)
    #d20 roll
    if arg == "d20":
        dice_result = random.randint(1,20)
    await ctx.send(dice_result)
    return

#COMMAND: boomerang, will repeat the argument if an argument is sent by the user
@client.command()
async def boomerang(ctx, *, arg):
    if arg:
        await ctx.send(arg)
    return

#COMMAND: knight, will respond with a phrase and knight the user
@client.command()
async def knight(ctx):
    #set role to Jedi Knight
    knightString = "By the will of the Force and the power granted to me, I Knight you young " + str(ctx.author) + " as a Jedi Knight! Now arise as a new child of the light. You will be the shield that guards innocents against those who would wish to cause harm."
    await ctx.send(knightString)

"""
print(str(client.guilds))
for guild in client.guilds:
        currentGuild = client.get_guild(guild.id)
        print(currentGuild.member_count)
        for x in range(0, currentGuild.member_count):
            member = currentGuild.members
            print(member[x].name, member[x].id)

"""

#COMMAND: collect data on detectable users.
@client.command()
async def customTest(ctx):
    usersData = {}

    #Check for a preexisting user database
    print("users.json exists = " + str(path.exists("users.json")))
    if path.exists('"users.json"'):
        with open('"users.json"') as usersDataFile:
            usersData = json.loads(usersDataFile.read())   
        print("Loaded users list:\n")
        for member in usersData:
            print(member)
    else:
        print("No user data detected.")

    #Check each scanned member against the pre-existing database
    for user in client.users:
        if usersData != None:
            detected = False
            for member in usersData:
                print("Comparing: " + member.name + " to " + member.name)
                if member.id == user.id:
                    detected = True
                    break
            if (detected == True):
                continue
            else:
                usersData[user.id] = user
        else:
            usersData[user.id] = user
            
    print("User list updated to:\n")
    for member in usersData:
        print(str(member) + " = " + str(usersData[member].name) + " " + str(usersData[member].id))

    #Write all of the data into the database
    with open("users.json", "w") as usersDataFile:
        json.dump(usersData, usersDataFile)

    #Confirm task completeion
    await ctx.send("Test Complete!")
    print("Test Complete!")
    return

def initialize():
    if path.exists("discordKeys.json"):
        with open("discordKeys.json", "r") as discordFile:
            Keys = json.load(discordFile)
            discordFile.close()
            print("Attempting to connect using the token: " + Keys["personalAssitant"]["botToken"])
            client.run(Keys["personalAssitant"]["botToken"])
    else:
        print("No discord keys were detected.")

initialize()