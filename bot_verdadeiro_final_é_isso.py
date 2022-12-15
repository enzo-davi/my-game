from estados_davi import estados, canais_de_voz
import discord
import random
from discord.ext import commands
from random import choice
from re import fullmatch
from os import getenv
from os.path import exists
from dotenv import load_dotenv
import pymongo

# Carregar variáveis de ambiente
load_dotenv()

# Iniciar base de dados com as definições do jogo
usuario = getenv('MONGODB_USERNAME', default='')
senha = getenv('MONGODB_PASSWORD', default='')
cluster = getenv('MONGODB_CLUSTER', default='')
uri = ''.join(['mongodb+srv://', usuario, ':', senha, '@', cluster, '/?retryWrites=true&w=majority'])
mongo_client = pymongo.MongoClient(uri)
database = mongo_client.chatbot
#
# Partidas
partidas_db = database.partidas

# Iniciar bot
intents = discord.Intents.default()
intents.message_content = True
prefix = '='
bot = commands.Bot(intents=intents, command_prefix=prefix)


@bot.event
async def on_ready():
    print('Pronto e iniciado')


@bot.event
async def on_message(msg):
    # autor = msg.author 
    # Testar se o autor é um bot (msg.author.bot é verdadeiro)
    # e, se for, simplesmente ignorar a mensagem
    if msg.author.bot:
        return
    autor = msg.author.id
    #
    # Filtrar comando por prefixo
    if msg.content.strip()[0] == prefix:
        mensagem = msg.content.strip()[1:]
    else:
        return
    #
    # Comandos que antecedem os demais: reiniciar
    if fullmatch('[rR]ecomeçar', mensagem):
        #
        # Pesquisar e apagar o registro no banco - e informar o usuário
        partidas_db.find_one_and_delete({'jogador': autor})
        await msg.channel.send("prontinho mano")
        return
    #
    # e fechar todos os canais de bot
    if fullmatch('[vV]aza', mensagem):
        #
        # Fechar todos os canais de voz
        [await canais_de_voz[i].disconnect() for i in canais_de_voz.keys()]
        await msg.channel.send("Flw.")
        return
    #
    # Garantir que o autor tem dados de partida
    if partidas_db.count_documents({'jogador': autor}) == 0:
        #
        # Jogador começa no estado 0 e inventário vazio
        partidas_db.insert_one({'jogador': autor, 
                                'estado': 0,
                                'aleatorio':0, 
                                'numero_de_perguntas':0,
                                'estados_passados':[],
                                'acertos':0,
                                'erros':0,
                                })
        
    #
    # Coletar os dados persistentes de usuário
    partida = partidas_db.find_one({'jogador': autor})
    
    print(f'partida {msg.author}: {partida["estado"]}')
    print(estados[partida['estado']]['proximos_estados'].items())
    
    #
    # Testar se o canal é pvt (msg.channel.type.name == 'private')
    # e, se for, avisar o jogador e continua o jogo sem áudio
    if msg.channel.type.name == 'private':
        #
        # Avisar ao jogador apenas quando o estado for 0
        if partida['estado'] == 0:
            await msg.channel.send("Não consigo entrar no canal pq é privado")
            await msg.channel.send("Não tem canal de voz pra eu entrar")
    #
    # Testar se a mensagem foi mandada em um chat de servidor
    # se sim, testar se o jogador está em canal de voz,
    # caso não esteja convidá-lo a entrar em um.
    if msg.channel.type.name != 'private':
        if msg.author.voice:
            if msg.guild.me not in msg.author.voice.channel.members:
                canais_de_voz[autor] = await msg.author.voice.channel.connect()
        else:
            await msg.channel.send("ENTRA NUM CANAL")
            return

    
        
    

    # Varrer os possíveis próximos estados para validar com a mensagem do usuário
    for key, value in estados[partida['estado']]['proximos_estados'].items():
        if fullmatch(key, mensagem):
            #
            # Atualiza o estado do jogador
            partida = partidas_db.find_one_and_update(
                {'jogador': autor},
                {'$set': {'estado': value}},
                return_document=pymongo.ReturnDocument.AFTER
            )
            print('estado atualizado')

            #Se o estado for 4000 é pra redirecionar o jogador para uma pergunta aleatória
            if partida['estado'] == 4000:
                # se for a primeira vez do jogador entrando no estado quatro mil o bot 
                # cria uma lista com o número de perguntas que o jogador vai ter
                if partida['aleatorio'] == 0:
                    #cria a lista que vai ser inserida no numero de perguntas
                    numeros = 5
                    
                    # muda o aleatorio pra 1 pro jogador não entrar mais dentro desse if e 
                    # coloca o numero de perguntas no banco de dados do jogador
                    partida = partidas_db.find_one_and_update({'jogador':autor},
                    {'$set':{'aleatorio':1,'numero_de_perguntas': numeros}},
                    return_document=pymongo.ReturnDocument.AFTER
                    )



                    print(partida['numero_de_perguntas'])
                
                # Checar se o número de perguntas não acabou
                if partida['numero_de_perguntas'] > 0:
                    # Escolhe um número aleatório com o número de estados.
                    estado_aleatorio = random.randint(10,39)
                    # Se o número já tiver sido escolhido antes continue ele continua sorteando.
                    if estado_aleatorio in partida['estados_passados']:
                        while estado_aleatorio in partida['estados_passados']:
                            
                            partida = partidas_db.find_one_and_update({'jogador':autor},
                    {'$set':{'estados_passados': partida['estados_passados'].append(estado_aleatorio), 'numero_de_perguntas': partida['numero_de perguntas'] - 1}},
                    return_document=pymongo.ReturnDocument.AFTER
                    )
                            estado_aleatorio = random.randint(10, 39)



                    partida = partidas_db.find_one_and_update({'jogador':autor},
                    {'$set':{'estado': estado_aleatorio}},
                    return_document=pymongo.ReturnDocument.AFTER
                    )
                #Se o número de perguntas for 0 quer dizer que o jogador acabou o quiz, 
                # então os erros e acertos são contabilizados.
                else:
                    erros = partida['erros']
                    acertos = partida['acertos']

                    await msg.channel.send(f'Você concluiu o quiz e acertou {acertos} de {erros + acertos}!\n\n')
                    


            #Quando o estado for 8(acertos) adicione acertos e subtraia do número de perguntas
            if partida['estado'] == 8:
                partida = partidas_db.find_one_and_update({'jogador':autor},
                    {'$set':{'acertos': partida['acertos'] + 1, 'numero_de_perguntas': partida['numero_de_perguntas'] - 1}},
                    return_document=pymongo.ReturnDocument.AFTER
                    )
            
            #Quando o estado for 9(erros) adicione erros e subtraia do número de perguntas
            if partida['estado'] == 9:
                partida = partidas_db.find_one_and_update({'jogador':autor},
                    {'$set':{'erros': partida['erros'] + 1, 'numero_de_perguntas': partida['numero_de_perguntas'] - 1}},
                    return_document=pymongo.ReturnDocument.AFTER
                    )






        #estado_do_jogador = estados[partida['estado']]   
        #estado_do_jogador = partida['estado'] 


            # Se houver um som referente ao estado,
            # toca no canal de voz do jogador
            if msg.channel.type.name != 'private':
                arquivo_de_som = str(value) + '.mp3'
                if exists(arquivo_de_som):
                    #
                    # Conectar no canal de áudio e emitir o som
                    som_opus = await discord.FFmpegOpusAudio.from_probe(arquivo_de_som)
                    canais_de_voz[autor].play(som_opus)
            #
            # Se houver uma imagem referente ao estado, enviar
            arquivo_de_imagem = str(value) + '.png'
            if exists(arquivo_de_imagem):
                await msg.channel.send(file=discord.File(arquivo_de_imagem))
            #
            # Criar uma lista de frases usando o delimitador '|' e enviar uma a uma
            #[await msg.channel.send()i for i in choice(estados[value]['frases']).split('|')]
            #  return

            
            await msg.channel.send(estados[partida['estado']]["frases"])
            return

    # Sempre responder ao usuário (dica ou não)
    #if partida['estado'] == 0:
    #   await msg.channel.send(estados[partida['estado']]['frases'])
    #else:
    await msg.channel.send(estados[partida["estado"]]["frases"])

        #await frase genérica...

bot.run(getenv('TOKEN_DO_BOT', default=''))