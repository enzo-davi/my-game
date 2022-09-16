from os import getenv, path
from dotenv import load_dotenv
import discord
import random
from discord.ext import commands
import gstreamer
load_dotenv()
# ali em cima eu importo tudo que eu vou usar no projeto, 
# já que se viesse tudo imbutido no python seria uma aplicação pesada demais
intents = discord.Intents.default()
intents.message_content = True
# Ficou feio essa lista ai, depois eu faço direitinho
lista_de_despedidas = ['escute seus pais', 'escove seus dentes', 
'estude bastante', 'tire notas boas', 'cuide de sua saúde', 'fumar faz mal','cuide da sua aparência', 'evite açúcar'
, 'não se envolva com más influências', 
'e lembre-se, não são os cabelos brancos que fazem o ancião; de qualquer velho que só tenha idade, pode-se dizer que envelheceu em vão',
'e lembre-se, um ancião é uma grande árvore que, já não tendo nem frutos nem folhas, ainda está presa à terra']

lista_de_imagens = ['batman.jpg', 'lagartixa.jpg', 'mordecai.jpg', 'trump.jpeg']
# aqui agnt cria o bot e seus comandos, o command prefix é o que vem antes de todos os comandos e os 
# intents são básicamente permissões do bot
bot = commands.Bot(intents=intents, command_prefix='!')

# esse bot event define como o bot vai reagir a um evento, 
# nesse caso quando o bot estiver pronto ele vai printar no console q ta preparado
@bot.event
async def on_ready():
    print('O Bot está preparado')
    print('------')

# Aqui agnt cria um comando, então se você digitar !join o bot entrará na call que você estiver, 
# já se você usar o comando e não estiver numa call o bot lhe avisará
@bot.command(pass_context= True)
async def iniciar(ctx):
    if (ctx.message.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('Entre numa call, rapaz, depois me chame.')




@bot.command(pass_context= True)
async def sair(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        frase_de_despedida = random.choice(lista_de_despedidas)
        await ctx.send(f'Adeus, {frase_de_despedida}, jovem.')
    else:
        await ctx.send('Eu não estou no VC, jovem.')

@bot.command(pass_context= True)
async def imagembolada(ctx):
    imagem_aleatoria = random.choice(lista_de_imagens)
    await ctx.send(file= discord.File(path.join("imagens", imagem_aleatoria)))





# esse comando inicia o bot, até antes daqui nenhuma linha de código foi executada, apenas funcionalidades foram definidas
bot.run(getenv("TOKEN_DO_BOT"))
