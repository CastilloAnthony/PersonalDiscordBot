import discord
import json
import random
import os
import math
import time
import calendar
import pathlib
currentPath = pathlib.Path(__file__).parent.resolve() # Gets the python script file's current location
os.chdir(currentPath) # Sets the working directory to the current file's location

from os import path
from discord.ext import commands
from bagOfDice_Imp import BagOfDice

intents = discord.Intents().all()
client = commands.Bot(command_prefix='!', intents=intents)
guilds = {}
usersDice = {}

@client.event
async def on_ready():
    print('Logged in as {0.user} with nickname {0.user.display_name}'.format(client))
    if client.user.name != 'personalassitant':
        await client.user.edit(username='personalassitant')
    for guild in client.guilds:
        guilds[guild.id] = guild.name
        bot = guild.get_member(client.user.id)
        if bot != None:
            await bot.edit(nick='Personal Assitant')
    print('Currently associated with these guilds: ', guilds)
    print("Current Latency: " + str(round(client.latency, 3)) + " seconds")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name='Project Zomboid | !pz'))
    # await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name='Project Zomboid'))
    return

@client.event
async def on_member_join(ctx):
    #client.command.scan()
    #await client.scan()
    return

@client.event
async def on_message(ctx):
    rndValue = random.randint(0, 9999)
    #print(rndValue)
    if (rndValue == 7777):
        message = 'cool story bro'
        await ctx.channel.send(message)
    if ctx.author.id == 258841431244800000: # Comrade Wolf's ID
        if (rndValue == 7):
            message = 'Nice!'
            await ctx.channel.send(message)
    elif ctx.author.id == 228794412921126912: # Comrade Gavin's ID
        if (rndValue == 7):
            message = 'Thats cute.'
            await ctx.channel.send(message)
    elif ctx.author.id == 234855562922295296: # Life Swordsman's ID
        if (rndValue % 10 == 5):
            message = 'cool story bro'
            await ctx.channel.send(message)
    else:
        if (rndValue == 99):
            message = 'oh yeah right'
            await ctx.channel.send(message)
    await client.process_commands(ctx)
    return

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send('Invalid command')

#COMMAND: remindme, reminds the user on the day and time specified 
@client.command()
async def remindme(ctx, arg):
    """WIP: Sends a message to a user at the day and time requested"""
    currentTime = time.gmtime(time.time())
    #print(currentTime[6]) # Day of the week (0-6), where 0 is monday
    await ctx.send("I will remind you on " + "Not Implemented")
    return

#COMMAND: ctime, will display the current time in a human readable format
@client.command()
async def ctime(ctx):
    """Says the current time in a human readable format"""
    await ctx.send(str(time.ctime()))
    return

#COMMAND: ping, will respond with pong and display the current latency
@client.command()
async def ping(ctx):
    """Displays the latency of this bot's responses"""
    await ctx.send("Pong!\n" + "Current Latency: " + str(round(client.latency, 3)) + " seconds.")
    return

#COMMAND: hello, will respond with 'world' 
@client.command()
async def hello(ctx):
    """Sends text message 'world'"""
    await ctx.send("world")
    return

#COMMAND: happy, will respond with the slight_smile emoji
@client.command()
async def happy(ctx):
    """Sends :slight_smile: Emoji"""
    await ctx.send(":slight_smile:")
    return

#COMMAND: boomerang, will repeat the argument if an argument is sent by the user
@client.command()
async def boomerang(ctx, *, arg):
    """Repeats what is said after the command"""
    if arg:
        await ctx.send(arg)
    return

'''
#COMMAND: dice, will send value found by random generation
@client.command()
async def dice(ctx, arg):
    """Roll Dice (type \"!dice help\" to see options)"""
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
'''

#COMMAND: dice, utilizes the dice framework, use !dice help for more info
@client.command()
async def dice(ctx, arg1 = None, arg2 = None, quantity = None):
    '''Utilizes the dice framework. Use !dice help for more info.'''
    if (str(ctx.author.id) in usersDice):
        if (arg1 == 'roll'): # Roll a dice
            if (arg2 != None):
                if (quantity != None):
                    message = str(usersDice[str(ctx.author.id)].rollDice(arg2, int(quantity)))
                    await ctx.send(message)
                    return
                else:
                    message = str(usersDice[str(ctx.author.id)].rollDice(arg2))
                    await ctx.send(message)
                    return
            else:
                message = str(usersDice[str(ctx.author.id)].rollDice())
                await ctx.send(message)
                return
        elif (arg1 == 'add'): # Adds a dice to the user's bag
            if (arg2 != None):
                if (usersDice[str(ctx.author.id)].addDice(arg2)):
                    message = 'Added ' + arg2 + ' to ' + str(ctx.author.id) + '\'s bag.'
                    await ctx.send(message)
                    return
                else:
                    message = 'Could not add ' + arg2 + ' to ' + str(ctx.author.id) + '\'s bag.'
                    await ctx.send(message)
                    return
            else:
                return
        elif (arg1 == 'remove'): # Removes a dice from the user's bag
            if (arg2 != None):
                if (usersDice[str(ctx.author.id)].removeDice(arg2)):
                    message = 'Removed ' + arg2 + ' from ' + str(ctx.author.id) + '\'s bag.'
                    await ctx.send(message)
                    return
                else:
                    message = 'Could not remove ' + arg2 + ' from ' + str(ctx.author.id) + '\'s bag.'
                    await ctx.send(message)
                    return
            else:
                return
        elif (arg1 == 'previous'): # Returns the previous rolled dice's result
            await ctx.send(str(usersDice[str(ctx.author.id)].getPrevious()))
            return
        elif (arg1 == 'history'): # Returns the history of all the dice that have been rolled from this bag
            await ctx.send(str(usersDice[str(ctx.author.id)].getHistory()))
            return
        elif (arg1 == 'empty'): # Empties the user's bag
            if (usersDice[str(ctx.author.id)].getHistory()):
                message = str(ctx.author.display_name) + '\'s dice bag has been empied.'
                await ctx.send(message)
                return
            else:
                message = 'Could not empty ' + str(ctx.author.display_name) + '\'s bag.'
                await ctx.send(message)
                return
        elif (arg1 == 'standardSet'): # Adds the standard DnD set of dice to the user's bag
            usersDice[str(ctx.author.id)].standardDiceSet()
            message = 'Added the standard DnD dice to ' + str(ctx.author.display_name) + '\'s bag.'
            await ctx.send(message)
            return
        elif (arg1 == 'display'): # Displays the dice in the bag and their last rolls
            message = str(ctx.author.display_name) +'\'s Bag: ' + str(usersDice[str(ctx.author.id)])
            await ctx.send(message)
            return
        elif (arg1 == 'help'): # Displays a message of the commands
            message = 'Utilization: !dice arg1, arg2, arg3 \narg1 can be one of the following commands: roll, add, remove, previous, history, empty, standardSet, display, or help \narg2 is be the number of faces for the dice you want to roll, add, or remove. \narg3 is the number of times you would like to roll your dice. \ni.e., !dice roll 6 4 will roll a d6 4 times.'
            await ctx.send(message)
            return
        else:
            return # Do nothing, no viable command was given
    else:
        message = str(ctx.author.display_name) + ' has no dice. Use !giveDice to get a set of dice.'
        await ctx.send(message)
        return # Do nothing if the user doesn't have a bag of dice.

#COMMAND: Gives a player a bag of dice
@client.command()
async def giveDice(ctx, name = None):
    '''Gives a bag of dice to the specified user'''
    message = ''
    if (name != None):
        for user in client.users:
            if (name in user.display_name):
                for i in usersDice:
                    if i == str(user.id):
                        message = str(name) + ' already has a bag of dice.'
                        await ctx.send(message)
                        return
                newBag = BagOfDice()
                newBag.standardDiceSet()
                print('Assigning a bag of dice to ', user.id)
                usersDice[str(user.id)] = newBag
                message = str(name) + ' has a new bag of dice to play with.'
                await ctx.send(message)
                return
        else:
            message = 'Could not give the user ' + str(name) + ' a bag of dice.'
            await ctx.send(message)
            return
    else:
        if (str(ctx.author.id) in usersDice):
            message = str(ctx.author.display_name) + ' already has dice.'
            return
        else:
            newBag = BagOfDice()
            newBag.standardDiceSet()
            print('Assigning a bag of dice to ', ctx.author.id)
            usersDice[str(ctx.author.id)] = newBag
            message = str(ctx.author.display_name) + ' has a new bag of dice to play with.'
            await ctx.send(message)
            return

#COMMAND: knight, will respond with a phrase and knight the user
@client.command()
async def knight(ctx, arg):
    """WIP: Changes a user's Role to Jedi Knight"""
    #set the user's role to Jedi Knight
    #print(ctx.author.roles)
    #print(ctx.message.guild.roles)
    print(discord.role)
    for role in ctx.message.guild.roles:
        authority = ''
        print(role)
        if "Admin" in role:
            authority = role
        print(authority)
        if authority in ctx.author.roles:
            knightString = "By the will of the Force and the power vested in me, I Knight you young " + str(ctx.author) + " as a Jedi Knight! Now arise as a new child of the light. You will be the shield that guards innocents against those who would wish to cause harm."
            await ctx.send(knightString)
    return

#COMMAND: changes a user's role to jedi
@client.command()
async def jedi(ctx, arg):
    """WIP: Changes a user's role to Jedi"""
    #set the user's role to Jedi
    jediString = "With the powers vested in me, I grant you the ranke of Padwan, " + arg
    await ctx.send(jediString)
    return

#COMMAND: changes a user's role to padwan
@client.command()
async def padwan(ctx, arg):
    """WIP: Changes a user's role to Padwan"""
    #set the user's role to Jedi
    padwanString = "With the powers vested in me, I grant you the ranke of Padwan, " + arg
    await ctx.send(padwanString)
    return

#COMMAND: changes a user's role to disciple
@client.command()
async def disciple(ctx, arg):
    """WIP: Changes a user's role to disciple"""
    #set the user's role to Jedi
    discipleString = "With the powers vested in me, I grant you the rank of disciple, " + arg
    await ctx.send(discipleString)
    return

#COMMAND: collect data on detectable users.
@client.command()
async def scan(ctx):
    """Initiates a scan of all the users in the server"""
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
                #print("Comparing: " + str(user.id) + " to " + str(usersData[member]["id"]))
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

#COMMAND: minecraft, gives out useful minecraft information to users who ask
@client.command(aliases=['mc'])
async def minecraft(ctx, arg1 = None):
    '''Will give out useful minecraft related information to users who ask.'''
    if (arg1 == None):
        message = 'For a list of commands use \'!mc help\''
        await ctx.send(message)
        return
    elif (arg1 == 'serverIp' or arg1 == 'ip'):
        ipAddress = '76.20.82.68'
        message = 'Here is the IP address of the server: ' + ipAddress
        await ctx.send(message)
        return
    elif (arg1 == 'help'):
        message = 'Available Commands: serverIP, ip'
        await ctx.send(message)
        return

#COMMAND: projectZomboid, gives out useful project zomboid information to users who ask
@client.command(aliases=['pz'])
async def projectZomboid(ctx, arg1 = None):
    '''Will give out useful project zomboid information to users who ask.'''
    if (arg1 == None):
        message = 'For a list of commands use \'!pz help\''
        await ctx.send(message)
        return
    elif (arg1 == 'game'):
        gameLink = 'https://projectzomboid.com/blog/'
        message = 'Here is a link to Project Zomboid\'s website: ' + gameLink
        await ctx.send(message)
        return
    elif (arg1 == 'mods'):
        packLink = 'https://steamcommunity.com/sharedfiles/filedetails/?id=2893925662'
        message = 'Here is a link to the current modpack: ' + packLink
        await ctx.send(message)
        return
    elif (arg1 == 'map'):
        mapLink = 'https://map.projectzomboid.com/'
        message = 'Here is a link to the online vanilla map: ' + mapLink
        await ctx.send(message)
        return
    elif (arg1 == 'serverIp' or arg1 == 'ip'):
        ipAddress = '76.20.82.68'
        port = '16261'
        message = 'Here is the IP address of the server: ' + ipAddress + ' and the port is ' + port
        await ctx.send(message)
        return
    elif (arg1 == 'news'):
        newsLink = 'https://projectzomboid.com/blog/news/'
        message = 'Here is a link to Vanilla Game News: ' + newsLink
        await ctx.send(message)
        return
    elif (arg1 == 'help'):
        message = 'Available Commands: mods, map, serverIP, ip, news'
        await ctx.send(message)
        return
    else:
        return
    
#COMMAND: change a user's nick name
@client.command(pass_context=True)
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

#This function will initialize our bot
def initialize():
    if path.exists("discordKeys.json"):
        #print('testing initialize')
        with open("discordKeys.json", "r") as discordFile:
            Keys = json.load(discordFile)
        print("Attempting to connect using the token: " + Keys["personalAssitant"]["botToken"])
        client.run(Keys["personalAssitant"]["botToken"])
    else:
        print("No discord keys were detected.")
    return

initialize()