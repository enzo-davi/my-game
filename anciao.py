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


async def tocar_som(msg,Nome_do_arquivo_do_som):
    if msg.channel.type.name != 'private':
        source = FFmpegPCMAudio(Nome_do_arquivo_do_som)
        await msg.author.voice.channel.play(source)




#mandar imagens com o file= discord.File('nome_da_file')
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
        
        await msg.channel.send("Progresso apagado")
        return
    #
    # e fechar todos os canais de bot
    if fullmatch('[dD]esconectar', mensagem):
        #
        # Fechar todos os canais de voz
        [await canais_de_voz[i].disconnect() for i in canais_de_voz.keys()]
        await msg.channel.send("Desconectando de todos os canais.")
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
                                'estados_disponiveis':[0],
                                'acertos':0,
                                'erros':0,
                                'streak':0,
                                'pontuação':0,
                                'tem_skip':0,
                                'comprou_skip':0,
                                'pegou_final':0,
                                })
    # fazer premios   


    # 100 pontos por pergunta
    # cada vez que o jogador acerta 3 seguidas ele ganha um multiplicador de pontuação de 2x

    #---Power Ups---#
    #
    # pular uma pergunta uma vez por partida--- 400
    #
    # final verdadeiro---- 5000


    # Coletar os dados persistentes de usuário
    partida = partidas_db.find_one({'jogador': autor})
    
    print(f'partida {msg.author} estado: {partida["estado"]}')
    # print(estados[partida['estado']]['proximos_estados'].items())
    
    
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
            await msg.channel.send("Entre num canal antes de começar o jogo.")
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
            

# Se o estado for 4001 mostre uma imagem  que depende da performance do jogador na partida
            if partida['estado'] == 4001:

                partida = partidas_db.find_one_and_update({'jogador':autor},
                    {'$set':{'aleatorio':0,
                    }},
                    return_document=pymongo.ReturnDocument.AFTER
                    )
                acertos = partida['acertos']
                if acertos <= 3:
                    await msg.channel.send("Por sua terrível performance, a equipe de produção o leva para uma ilha deserta, a fim de que você tenha muito tempo para pensar sobre seus atos.", file = discord.File('ilha_deserta.jpg'))
                elif acertos <= 5:
                    await msg.channel.send('Você foi mal, mas não o suficiente para me causar grande desapontamento.\n\n Pela sua performance hoje, você recebe uma estrela.', file = discord.File('estrela.jpg'))
                elif acertos <=7:
                    await msg.channel.send('Sua performance me deixou completamente neutro. Você não foi bem e nem mal, bem vindo ao clube da mediocridade.', file = discord.File('meh.jpg'))
                elif acertos <= 9:
                    await msg.channel.send('Sua performance foi como sentir a fresca brisa do mar, como quando você come uma comida excepcionalmente boa, ou até mesmo como quando você chega em casa e retira os calçados.\n\nPelo seu esforço, você ganha um travesseiro que sempre mantém os dois lados numa temperatura agradável.', file = discord.File('travesseiro.jpg'))
                elif acertos == 10:
                    await msg.channel.send('Você superou absolutamente todas as minhas expectativas. A plateia exclama seu nome com emoção e júbilo, exaltando-o como o melhor de todos os tempos.', file = discord.File('trofeu levante.png'))
                    


            #Se o estado for 4000 é pra redirecionar o jogador para uma pergunta aleatória
            if partida['estado'] == 4000:
                # se for a primeira vez do jogador entrando no estado quatro mil o bot 
                # define o numero de perguntas
                if partida['aleatorio'] == 0:
                    #
                    numeros = 10
                    # Cria uma lista com o numero de estados e coloca na database
                    lista_estados_disponiveis = list(range(10,48))
                    # muda o aleatorio pra 1 pro jogador não entrar mais dentro desse if e 
                    # coloca o numero de perguntas no banco de dados do jogador
                    partida = partidas_db.find_one_and_update({'jogador':autor},
                    {'$set':{'aleatorio':1,'numero_de_perguntas': numeros,
                    'estados_disponiveis': lista_estados_disponiveis,
                    }},
                    return_document=pymongo.ReturnDocument.AFTER
                    )
                    #
                    #
                    print(partida['numero_de_perguntas'])
                #
                # Checar se o número de perguntas não acabou
                if partida['numero_de_perguntas'] > 0:
                    #
                    lista_estados_disponiveis = partida['estados_disponiveis'].copy()
                    random.shuffle(lista_estados_disponiveis)
                    estado_aleatorio = lista_estados_disponiveis.pop(0)
                    
                    # atualiza o jogador pro estado aleatório e atualiza a lista de estados disponiveis
                    partida = partidas_db.find_one_and_update({'jogador':autor},
                    {'$set':{'estado': estado_aleatorio,
                    'estados_disponiveis': lista_estados_disponiveis, 
                    }},
                    return_document=pymongo.ReturnDocument.AFTER
                    )
                #Se o número de perguntas for 0 quer dizer que o jogador acabou o quiz, 
                # então os erros e acertos são contabilizados.
                else:
                    erros = partida['erros']
                    acertos = partida['acertos']

                    await msg.channel.send(f'Você concluiu o quiz e acertou {acertos} de {erros + acertos}!\n\n')
                    


            #Quando o estado for 8(acertos) adicione acertos e subtraia do número de perguntas
            #Como o return acontecerá dentro dos estados de acerto e erro não enviaremos imagens ou sons 
            if partida['estado'] == 8:
                numero_perguntas = partida['numero_de_perguntas'] - 1
                partida = partidas_db.find_one_and_update({'jogador':autor},
                {'$set':{'streak': partida['streak'] + 1, 
                'numero_de_perguntas': numero_perguntas}},
                return_document=pymongo.ReturnDocument.AFTER
                )

                # Se o jogador acertar 3 ou mais perguntas seguidas ele ganha 200 pontos pela pergunta
                if partida['streak'] >= 3:
                    partida = partidas_db.find_one_and_update({'jogador':autor},
                        {'$set':{'acertos': partida['acertos'] + 1,
                        'pontuação': partida['pontuação'] + 200,
                        }},
                        return_document=pymongo.ReturnDocument.AFTER
                        )
                    streak = partida['streak']
                    pontuação = partida['pontuação']
                    acertos = partida['acertos']
                    erros = partida['erros']
                    await msg.channel.send(f'Acertou!\n\n Você está numa streak de {streak} acertos e acertou {acertos} de {acertos + erros}.\n\n {pontuação} pontos.\n\n Continuar(1)')
                    return            
                #Se o jogador não estiver na streak ele ganha 100 pontos.    
                else:
                    partida = partidas_db.find_one_and_update({'jogador':autor},
                        {'$set':{'acertos': partida['acertos'] + 1,
                        'pontuação': partida['pontuação'] + 100,
                        }},
                        return_document=pymongo.ReturnDocument.AFTER
                        )
                    pontuação = partida['pontuação']
                    acertos = partida['acertos']
                    erros = partida['erros']
                    await msg.channel.send(f'Acertou!\n\n Você acertou {acertos} de {acertos + erros}.\n\n {pontuação} pontos.\n\n Continuar(1)')
                    return


                
            #Quando o estado for 9(erros) zere a streak, adicione erros e subtraia do número de perguntas
            if partida['estado'] == 9:
                numero_perguntas = partida['numero_de_perguntas'] - 1
                partida = partidas_db.find_one_and_update({'jogador':autor},
                    {'$set':{'erros': partida['erros'] + 1, 
                    'numero_de_perguntas': numero_perguntas,
                    'streak':0,
                    }},
                    return_document=pymongo.ReturnDocument.AFTER
                    )
                pontuação = partida['pontuação']
                acertos = partida['acertos']
                erros = partida['erros']    
                await msg.channel.send(f'Errou.\n\n Você acertou {acertos} de {acertos + erros}.\n\n {pontuação} pontos.\n\n Continuar(1)')
                

            if partida['estado'] == 101 and partida['comprou_skip'] == 0 and partida['pontuação'] >= 400:
                partida = partidas_db.find_one_and_update({'jogador':autor},
                    {'$set':{'comprou_skip':1,
                    'pontuação': partida['pontuação'] - 400,
                    }},
                    return_document=pymongo.ReturnDocument.AFTER
                    )
                await msg.channel.send('Power up comprado com sucesso, para voltar para a loja digite (1)')
            elif partida['estado'] == 101 and partida['comprou_skip'] == 1:
                await msg.channel.send('Você já comprou este power up, para voltar para a loja digite (1)')
            elif partida['estado'] == 101 and partida['comprou_skip'] == 0 and partida['pontuação'] < 400:
                await msg.channel.send('Você não tem pontos o suficiente para compar este power up, para voltar para a loja digite (1)')



            
            if partida['estado'] == 0:
                partida = partidas_db.find_one_and_update({'jogador':autor},
                    {'$set':{'acertos':0,
                    'erros': 0,
                    'numero_de_perguntas':0,
                    'aleatorio': 0,
                    'streak': 0,
                    }},
                    return_document=pymongo.ReturnDocument.AFTER
                    )
                if partida['comprou_skip'] == 1:
                    partida = partidas_db.find_one_and_update({'jogador':autor},
                    {'$set':{'tem_skip':1,
                    }},
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
                    canais_de_voz[msg.author.id].play(som_opus)
            #
            # Se houver uma imagem referente ao estado, enviar
            arquivo_de_imagem = str(value) + '.png'
            if exists(arquivo_de_imagem):
                await msg.channel.send(file=discord.File(arquivo_de_imagem))
            #
            # Criar uma lista de frases usando o delimitador '|' e enviar uma a uma
            #[await msg.channel.send()i for i in choice(estados[value]['frases']).split('|')]
            #  return

            if partida['estado'] == 100:
                pontos = partida['pontuação']
                await msg.channel.send(estados[partida['estado']]["frases"] + f'Pontuação: {pontos}' )
                return


            if partida['estado'] == 1000:
                pontos = partida['pontuação']
                if pontos >= 2000:
                    await msg.channel.send(estados[partida['estado']]["frases"])
                    return
                else:
                    await msg.channel.send('Você não tem pontos o suficiente para comprar o final verdadeiro, volte com mais pontos\n\n (4)Voltar.')
                    return

            if partida['estado'] == 1006:
                frase = estados[partida['estado']]["frases"]
                await msg.channel.send(frase, file = discord.File('véio.png'))
                return





            
            await msg.channel.send(estados[partida['estado']]["frases"])
            
                
            return
            


    #Sempre responder ao jogador
    await msg.channel.send(estados[partida["estado"]]["frases"])



bot.run(getenv('TOKEN_DO_BOT', default=''))
