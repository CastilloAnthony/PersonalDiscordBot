import discord
import json
import random
import os

from os import path
from discord.ext import commands

Keys = {}
usersData = {}

client = commands.Bot(command_prefix='!')
currentGuild = discord.Guild

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

#COMMAND: collect data on detectable users.
@client.command()
async def customTest(ctx):
    #Check for a preexisting user database
    if path.exists("users.json"):
        with open("users.json", "r") as file:
            usersData = json.load(file)    
        print("Users List:\n")
        for i, k in usersData:
            print(i, k, "\n")
    else:
        print("No user data detected.")

    #Check each scanned member against the pre-existing database
    for i in client.get_all_members():
        k
        for k in usersData:
            if i == k:
                break
        if (k != None) or (k == i):
            continue
        else:
            usersData.append(i)

    #Write all of the data into the database
    with open("users.json", "w") as file:
        json.dump(usersData, file)
        print("User list updated to:\n" + json.dump(usersData) + "\n")

    #Confirm task completeion
    await ctx.send("Test Complete!")
    print("Test Complete!")
    return

def initialize():
    if path.exists("discordKeys.json"):
        with open("discordKeys.json", "r") as file:
            Keys = json.load(file)
            file.close()
            print("Attempting to connect using the token: " + Keys["personalAssitant"]["botToken"])
            client.run(Keys["personalAssitant"]["botToken"])
    else:
        print("No discord keys were detected.")

initialize()