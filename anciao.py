from os import getenv, path
from dotenv import load_dotenv
import discord
from discord import FFmpegPCMAudio
import random
import asyncio
from discord.ext import commands
load_dotenv()

imagens = ['batman.jpg','lagartixa.jpg','mordecai.jpg','trump.jpeg']

class MyBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        channel = message.channel

        if message.author.id == self.user.id:
            return
        sent = await message.reply('oiii!!!!111')
        await sent.add_reaction("✅")
        await sent.add_reaction("❌")



        async def check(reaction, user):
            return user != message.author and str(reaction.emoji) == '✅'
        
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=120.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')    



intents = discord.Intents.default()
intents.message_content = True

client = MyBot(intents=intents)
client.run(getenv("TOKEN_DO_BOT"))
