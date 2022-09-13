from os import getenv, path
from dotenv import load_dotenv
import discord
import random
from discord.ext import commands
load_dotenv()
#ali em cima eu importo tudo que eu vou usar no projeto, já que se viesse tudo imbutido no python seria uma aplicação pesada demais
intents = discord.Intents.default()
intents.message_content = True

#
bot = commands.Bot(intents=intents, command_prefix='!')


@bot.event
async def on_ready():
    print('O Bot está preparado')
    print('------')


@bot.command(pass_context= True)
async def join(ctx):
    if (ctx.message.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('entra na call')


bot.run(getenv("TOKEN_DO_BOT"))
