from os import getenv, path
from dotenv import load_dotenv
import discord
from discord import FFmpegPCMAudio
import random
from discord.ext import commands
load_dotenv()

imagens = ['batman.jpg','lagartixa.jpg','mordecai.jpg','trump.jpeg']

class MyBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('.'):
            await message.reply('bingos bongos',file= discord.File(path.join('imagens', random.choice(imagens))),mention_author=True)





intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(getenv("TOKEN_DO_BOT"))
