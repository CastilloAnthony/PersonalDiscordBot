import discord
from discord.ext import commands


discordPublicId = "9198975fb26be78918e25d31e4efdbf1e6f7d4defc83a9d2de191fbe92bd4f52"
bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('token')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run('token')