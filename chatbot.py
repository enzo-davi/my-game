from os import getenv
from dotenv import load_dotenv
import discord
load_dotenv()

import random
imagens = ['imagem.png','imagem1.jpeg','imagem2.jpeg','imagem3.jpeg']

import random
lista_juca = ['melancia com mel', 'the rock cocaina' , 'pequenoi grande anão' , 'pimenta com granola' , 'falo tudo que penso']
lista_enzo = ['branquinho básico']
lista_davi = ['davi não pegue']
lista_nico = ['nariz']
lista_pedro = ['alcólatra']
lista_vi = ['bebado triste']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('.juca'):

            await message.reply(random.choice(lista_juca), mention_author=True)
            await message.reply(file= discord.File(random.choice(imagens)),mention_author=True)

        if message.content.startswith('.enzo'):
            await message.reply(random.choice(lista_enzo), mention_author=True)
            await message.reply(file= discord.File(random.choice(imagens)),mention_author=True)

        if message.content.startswith('.davi'):
            await message.reply(random.choice(lista_davi), mention_author=True)
            await message.reply(file= discord.File(random.choice(imagens)),mention_author=True)

        if message.content.startswith('.nico'):
            await message.reply(random.choice(lista_nico), mention_author=True)
            await message.reply(file= discord.File(random.choice(imagens)),mention_author=True)

        if message.content.startswith('.pedro'):
            await message.reply(random.choice(lista_pedro), mention_author=True)
            await message.reply(file= discord.File(random.choice(imagens)),mention_author=True)

        if message.content.startswith('.vi'):
            await message.reply(random.choice(lista_vi), mention_author=True)
            await message.reply(file= discord.File(random.choice(imagens)),mention_author=True)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(getenv("DISCORD_TOKEN"))