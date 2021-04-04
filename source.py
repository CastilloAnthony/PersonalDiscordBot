import discord
from discord.ext import commands


discordPublicId = "9198975fb26be78918e25d31e4efdbf1e6f7d4defc83a9d2de191fbe92bd4f52"

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(discordPublicId)
