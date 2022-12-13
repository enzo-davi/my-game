from os import getenv, path
from dotenv import load_dotenv
import discord
from discord import FFmpegPCMAudio
import random
import asyncio
from os.path import exists
from re import fullmatch
from estados_davi import estados, partidas
from discord.ext import commands
load_dotenv()

imagens = ['batman.jpg','lagartixa.jpg','mordecai.jpg','trump.jpeg']




class MyBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, msg):
        # we do not want the bot to reply to itself
        channel = msg.channel
        autor = msg.author.id

        if msg.author.bot:
            return
        
        #LEMBRA DE DESCOMENTAR ISSO DPS if autor not in partidas:
        #
        # Jogador começa no estado 0 com duas chaves
        partidas[autor] = {
            'estado': 0,
            'inventario': {
                'chave_prateada',
                'chave_dourada'
                }
        }
        

        estado_do_jogador = estados[partidas[autor]['estado']]
        inventario_do_jogador = partidas[autor]['inventario']
        
        for key, value in estado_do_jogador['proximos_estados'].items():
            if fullmatch(key, msg.content):
                
                if estado_do_jogador == 2:
                    exit()
                
                
                #
                # Verificar se o jogador possui inventário mínimo para avançar
                if inventario_do_jogador.issuperset(estados[value]['inventario']):
                    #
                    # Atualiza o estado do jogador
                    partidas[autor]['estado'] = value
                    
                    
                    


                    #
                    # Remove os itens de inventário requisitados
                    #partidas[autor]['inventario'] = inventario_do_jogador.difference(
                        #estados[value]['inventario'])
                    #
                    # Se houver uma imagem referente ao estado,
                    # envia essa primeiro
                    imagem = str(value) + '.png'
                    if exists(imagem):
                        await msg.channel.send(file=discord.File(imagem))
                    #
                    # Se houver um som referente ao estado,
                    # toca no canal de voz do jogador
                    som = str(value) + '.opus'
                    if exists(som):
                        # canal_de_voz.play(AudioSource)
                        pass
                    
                    # Cria uma lista de frases usando o delimitador '|' e envia uma a uma

                    await msg.channel.send(estados[value]["frases"])

                else:
                    #
                    # Retornar mensagem (e manter jogador no atual estado)
                    await msg.channel.send(frases['inventario_insuficiente'])
                return



        
        


     #   async def check(reaction, user):
      #      return user != msg.author and str(reaction.emoji) == '✅'
       # 
        #    reaction, user = await client.wait_for('reaction_add', check=check)
        #except asyncio.TimeoutError:
        #    await channel.send('👎')
        #else:
        #    await channel.send('👍')

intents = discord.Intents.default()
intents.message_content = True

client = MyBot(intents=intents)
client.run(getenv("TOKEN_DO_BOT"))
