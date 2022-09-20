from os import getenv, path
from dotenv import load_dotenv
import discord
from discord import FFmpegPCMAudio
import random
from discord.ext import commands
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





estados = {
    0: {
            "frases":["Digite 'grito'!"],
            "proximos_estados":{"grito": 1}
    },

    1:{ 
            "frases":["Uma vez eu acordei de um sonho horrível.\nEu estava sentado no sofá da sala, junto de meu pai, eu podia escutar sua respiração, ele dormia também.\nAo acordá-lo para contar meu sonho, ele resmunga algumas palavras ininteligíveis, eu assumi que seu cansaço era devido à minha súbita interrupção de seu sono profundo.\n\"Acorde pai! Eu tenho medo, meu sonho foi muito ruim.\"\nDe repente, as luzes se acendem, eu olho para ver quem acendeu o interruptor, e encontro ninguém mais e ninguém menos do que meu próprio pai, em pé, mão direita no interruptor, expressão neutra e pupilas dilatadas como se não houvesse vida naqueles olhos.\nOlhando de volta para o sofá, meu pai já não está mais lá.\nA TV liga sozinha, e o barulho de estática torna-se horrivelmente alto.\nEu [[grito]].\nO que aconteceu?"],
            "proximos_estados":{}
    }
}








#dicionario das partidas do jogador
partidas = {}


@bot.event
async def on_ready():
    print('O Bot está preparado')
    print('------')


@bot.command(pass_context= True)
async def iniciar(ctx):
    if (ctx.message.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('interior_ambiance.mp3')
        player = voice.play(source)
        await ctx.message.channel.send('olá')
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


@bot.event
async def on_message(msg):
    # Verificar se a mensagem não tem o próprio bot como autor.
    #if msg.author.id == msg.channel.me.id:
    #    return

    # Verificar se o jogador ainda não começou a partida,
    # o que significa que precisa colocá-lo no estado zero (0).
    if msg.author.id not in partidas:
        partidas[msg.author.id] = 0

    # Em ordem de operação:
    # 0) Obter o ID do jogador:
    #    msg.author.id
    # 1) Obter o estado atual do jogador:
    #    partidas[msg.author.id]
    # 2) Obter a definição completa desse estado:
    #    estados[partidas[msg.author.id]]
    # 3) Filtrar desse estado apenas a lista de próximos estados:
    #    estados[partidas[msg.author.id]]['proximos_estados']
    # 4) Filtrar dessa lista as chaves (frases) quem levam a próximos estados:
    #    estados[partidas[msg.author.id]]['proximos_estados'].keys()
    # 5) Verificar se a frase do usuário está na lista de chaves (frases) do estado:
    if msg.content in estados[partidas[msg.author.id]]['proximos_estados'].keys():
        #
        # 6) Atualizar o estado do jogador, fazendo-o avançar no jogo:
        partidas[msg.author.id] = estados[partidas[msg.author.id]]['proximos_estados'][msg.content]
        #
        # 7) Enviar para o jogador a mensagem do estado (já atualizado)
        #
        # Em ordem de operação:
        # 7.0) Obter o ID do jogador:
        #    msg.author.id
        # 7.1) Obter o estado atual do jogador:
        #    partidas[msg.author.id]
        # 7.2) Obter a definição completa desse estado:
        #    estados[partidas[msg.author.id]]
        # 7.3) Filtrar desse estado apenas a lista de frases:
        #    estados[partidas[msg.author.id]]['frases']
        # 7.4) Sortear uma frase dessa lista:
        #   choice(estados[partidas[msg.author.id]]['frases'])
        await msg.channel.send(random.choice(estados[partidas[msg.author.id]]['frases']))
    #
    # Caso contrário, avisar que a mensagem não avança no jogo
    else:
        #
        # Se o jogador está no primeiro estado...
        if partidas[msg.author.id] == 0:
            #
            # ...ajudar com uma dica:
            await msg.channel.send(random.choice(estados[partidas[msg.author.id]]['frases']))
        else:
            #
            # Nos estados seguintes, a resposta padrão de HAL:
            await msg.channel.send('I\'m sorry Dave, I\'m afraid I can\'t do that.')






# esse comando inicia o bot, até antes daqui nenhuma linha de código foi executada, apenas funcionalidades foram definidas
bot.run(getenv("TOKEN_DO_BOT"))
