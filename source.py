import discord
import json
import random
import os
import math

from os import path
from discord.ext import commands

Keys = {}

intents = discord.Intents().all()
client = commands.Bot(command_prefix='!', intents=intents)
#currentGuild = discord.Guild

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("Current Latency: " + str(round(client.latency, 3)) + " seconds")
    #readFileJson("users.json", usersData)
    #print(str(currentGuild))

@client.command()
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommmandNotFound):
		await ctx.send('Invalid command')

#COMMAND: ping, will respond with pong and display the current latency
@client.command()
async def ping(ctx):
    await ctx.send("Pong!" + " Current Latency: " + str(round(client.latency, 3)) + " seconds.")
    return

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

#COMMAND: boomerang, will repeat the argument if an argument is sent by the user
@client.command()
async def boomerang(ctx, *, arg):
    if arg:
        await ctx.send(arg)
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

#COMMAND: knight, will respond with a phrase and knight the user
@client.command()
async def knight(ctx, arg):
    #set the user's role to Jedi Knight
    knightString = "By the will of the Force and the power granted to me, I Knight you young " + str(ctx.author) + " as a Jedi Knight! Now arise as a new child of the light. You will be the shield that guards innocents against those who would wish to cause harm."
    await ctx.send(knightString)

#COMMAND: collect data on detectable users.
@client.command()
async def scanForNew(ctx):
    usersData = {}
    newUsers = 0
    print("Scannning for new users.")
    #Check for a pre-existing user database
    if path.exists("users.json"):
        with open("users.json") as usersDataFile:
            usersData = json.load(usersDataFile)
        print("Loaded users list:\n")
        for member in usersData:
            print(member)
    else:
        print("No user data detected.")

    print("\n")
    #Check each scanned member against the pre-existing database
    for user in client.users:
        if usersData != None:
            detected = False
            for member in usersData:
                print("Comparing: " + str(user.id) + " to " + str(usersData[member]["id"]))
                if user.id == usersData[member]["id"]:
                    detected = True
                    print("The user " + user.name + "#" + user.discriminator + " is already registered.")
                    break
            if (detected == True):
                continue
            else:
                tempString = user.name + "#" + user.discriminator
                usersData[tempString] = {
                "id" : user.id,
                "name" : user.name,
                "discriminator" : user.discriminator,
                "display_name" : user.display_name,
                "bot" : user.bot,
                "created_at" : str(user.created_at),
                "color" : user.color.value,
                "mention" : user.mention,
                "avatar" : user.avatar
                }
                newUsers = newUsers + 1
                print("Added " + tempString + " to the list.")
        else:
            tempString = user.name + "#" + user.discriminator
            usersData[tempString] = {
            "id" : user.id,
            "name" : user.name,
            "discriminator" : user.discriminator,
            "display_name" : user.display_name,
            "bot" : user.bot,
            "created_at" : str(user.created_at),
            "color" : user.color.value,
            "mention" : user.mention,
            "avatar" : user.avatar
            }
            print("Added " + tempString + " to the list.")
            newUsers = newUsers + 1

    #Write all of the data into the database
    with open("users.json", "w") as usersDataFile:
        json.dump(usersData, usersDataFile, indent=0, sort_keys=True)

    #Print out the results
    if newUsers == 0:
        print("No new users were added to the list.")
    else:
        print("\nUser list updated to:")
        for member in usersData:
            print(str(member) + " with user id " + str(usersData[member]["id"]))
        print("With " + str(newUsers) + " new users registered.")

    #Confirm task completeion
    await ctx.send("Scan Complete!")
    print("Scan Complete!\n")
    return

#This function will initialize our bot
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