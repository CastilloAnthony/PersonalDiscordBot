import discord
import json
from discord.ext import commands

discordKeys = { 
    "clientID" : "825455539399557181",
    "publicKey" : "9198975fb26be78918e25d31e4efdbf1e6f7d4defc83a9d2de191fbe92bd4f52",
    "botToken" : "ODI1NDU1NTM5Mzk5NTU3MTgx.YF-LYA.dfYIofb-fVLbcBMUb22CE3EU_LM",
    "redirect-URL" : "https://www.swtor.com/"
    }

client = commands.Bot(command_prefix='!')
currentGuild = discord.Guild()
client = discord.Client()

def getDiscordUsers():
    guildSize = len(client.users)
    usersList = {}
    print(guildSize)
    for i in client.users:
        usersList[client.users] = client.users[i]
    f = open("users.json", "w")
    f.write(json.dumps(usersList, sort_keys=True))
    f.close()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    getDiscordUsers()

@client.event
async def on_message(ctx):
    if ctx.author == client.user:
        return

    if ctx.content.startswith('!'):
        if ctx.content.find("hello") != -1:
            await ctx.channel.send('Hello!')
        elif ctx.content.find("knight") != -1:
            #set their role to Jedi Knight
            knightString = "I Knight you young " + str(ctx.author) + ". Now arise as a new Jedi Knight! You will act as a shield guarding innocents against those who would wish to cause harm."
            await ctx.channel.send(knightString)

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommmandNotFound):
		await ctx.send('Invalid command')

client.run(discordKeys["botToken"])