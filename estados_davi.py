estados = {
    
#Tutorial

    0: {
        "frases":"Iniciar o jogo?\n\n SIM(1)\n NÃO(2)\n Pular Tutorial(3)\n", 
        "proximos_estados":{
        "1":1,
        "2":2,
        "3":4000,
        },
        "inventario":{}
            
},

    1: {
        "frases":"Bem vindo(a)!\n\n Nesse Quiz será feito 30 perguntas variando de nível fácil a difícil, e seu objetivo é acertar o maior número possível. Você terá respostas de múltipla escolha, no qual apenas UMA estará correta. Para escolher uma alternativa digite um dos números referentes a alternativa.\n\n Continuar tutorial(1)\n ", 
        "proximos_estados":{
        "1":3
        },
        "inventario":{}
},

    2:{
        "frases":"Desconectando.",
        "proximos_estados":{},
        "inventario":{}
},

    3:{
        "frases":'Quantas asas tem um pombo ?\n\n Duas(1)\n Dez(2)\n Vinte(3)\n Quarenta(4)\n',
        "proximos_estados":{
        "1":4,
        "2":5,
        "3":5,
        "4":5,
        },
        "inventario":{}
},

    4:{
        "frases":"Acertou!\n\n Continuar(1)\n",
        "proximos_estados":{
        "1":6,
        },
        "inventario":{}
},

    5:{
        "frases":"Errou!\n\n Continuar(1)\n",
        "proximos_estados":{
        "1":6,
        },
        "inventario":{}
},

    6:{
    "frases":" Agora que você entendeu como funciona, iniciará o Quiz definitivo, no qual contabilizará seus acertos.\n\n Finalizar tutorial(1)\n",
    "proximos_estados":{
        "1":4000,
        },
        "inventario":{}
},

# Fim do tutorial      

#Estados especiais de acerto e derrota

    8:{
        "frases":"Acertou!\n\n Continuar(1)\n",
        "proximos_estados":{
        "1":4000
        }
},

    9:{
        "frases":"Errou!\n\n Continuar(1)\n",
        "proximos_estados":{
        "1":4000
        }
},

#estados do GAME

    10:{
        "frases":"Quantos paises são reconhecidos pela ONU ?\n\n 206(1)\n 211(2)\n 193(3)\n 184(4)\n",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":8,
        "4":9,
        },
        "inventario":{}
},

    11:{
    "frases":"Quantas copas tem o Brasil ?\n\n 4(1)\n 5(2)\n 6(3)\n Nenhuma(4)\n",
    "proximos_estados":{
        "1":9,
        "2":8,
        "3":9,
        "4":9,
        },
        "inventario":{}
},  

    12:{
        "frases":"Quantos estados tem o Brasil, contando o distrito federal ?\n\n 25(1)\n 26(2)\n 27(3)\n 28(4)\n",
    "proximos_estados":{
        "1":9,
        "2":9,
        "3":8,
        "4":9,
        },
        "inventario":{}
},

    13:{
        "frases":"Quem foi o único Presidente brasileiro eleito com sufrágio universal que nasceu em São Paulo ?\n\n Lula(1)\n Collor(2)\n Sarnei(3)\n Bolsonaro(4)\n",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":9,
        "4":8,
        },
        "inventario":{}
},  

    14:{
        "frases":"Qual é a capital da Croácia ?\n\n Zagrebe(1)\n Berlim(2)\n Saravejo(3)\n Belgrado(4)",
        "proximos_estados":{
        "1":8,
        "2":9,
        "3":9,
        "4":9,
        },
        "inventario":{}
},

    15:{
        "frases":"Qual das alternativas não é uma planta ?\n\n Gigoga(1)\n Congonha(2)\n Lírio Almiscarado(3)\n Gafanhoto(4)\n",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":9,
        "4":8,
        },
        "inventario":{}
},

    16:{
        "frases":"Quantos continentes tem no planeta terra ?\n\n 4(1)\n 5(2)\n 6(3)\n Nehuma das alternativas(4)\n",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":8,
        "4":9,
        },
        "inventario":{}
},  

    17:{
        "frases":"Dia da independência do Brasil ?\n\n 22(1)\n 17(2)\n 13(3)\n 11(4)\n",
        "proximos_estados":{
        "1":8,
        "2":9,
        "3":9,
        "4":9,
        },
        "inventario":{}
},

    18:{
        "frases":"Quantos planetas tem no sistema solar ?\n\n 7(1)\n 8(2)\n 9(3)\n 10(4)\n",
        "proximos_estados":{
        "1":9,
        "2":8,
        "3":9,
        "4":9,
        },
        "inventario":{}
},  

    19:{
        "frases":"Quem assinou a Lei Aurea ?\n\n Dom Pedro I(1)\n Dom Pedro II(2)\n Dom João VI(3)\n Princesa Isabel(4)\n",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":9,
        "4":8,
        },
        "inventario":{}
}, 

    20:{
        "frases":"Quantos filmes tem a franquia Veloses e Furiosos até o ano de 2022 ?\n\n 7(1)\n 8(2)\n 9(3)\n 10(4)\n",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":8,
        "4":9,
        },
        "inventario":{}
}, 

    21:{
        "frases":"Em que ano começou e terminou a ditadura militar no Brasil ?\n\n 1914-1918(1)\n 1964-1985(2)\n 1939-1945(3)\n 1947-1991(4)\n",
        "proximos_estados":{
        "1":9,
        "2":8,
        "3":9,
        "4":9,
    },
    "inventario":{}
},

    22:{
        "frases":"Qual o melhor jogo do ano 2022 ?\n\n God of War Ragnarok(1)\n Horizon Forbidden West(2)\n Elden ring(3)\n Nenhuma das alternativas(4)\n",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":8,
        "4":9,
        },
        "inventario":{}
},  

    23:{
        "frases":"Qual dos impérios a seguir não possui um idioma escrito ?\n\n Inca(1)\n Azteca(2)\n Egípcio(3)\n Romano(4)\n",
        "proximos_estados":{
        "1":8,
        "2":9,
        "3":9,
        "4":9,
        },
        "inventario":{}
},

    24:{
        "frases":"Até 1923, como era chamada a cidade turca de Istambul?\n\n Tijolo(1)\n Goldenvale(2)\n Constantinopla(3)\n Edensville(4)\n",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":8,
        "4":9,
        },
        "inventario":{}
},  

    25:{
        "frases":"Quantos dias a terra leva para orbitar o sol, em ano bissesto ?\n\n 7(1)\n 31(2)\n 365(1)\n 366(4)\n",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":9,
        "4":8,
        },
        "inventario":{}
},

    26:{
        "frases":"Qual é o menor país do mundo ?\n\n Mônaco(1)\n Vaticano(2)\n Nauru(3)\n Gales(4)",
        "proximos_estados":{
        "1":9,
        "2":8,
        "3":9,
        "4":9,
        },
        "inventario":{}
},

    27:{
        "frases":" Qual é o rio mais longo do mundo ?\n\n Nilo(1)\n Amazonas(2)\n Mississippi(3)\n Yangtzé(4)\n",
        "proximos_estados":{
        "1":8,
        "2":9,
        "3":9,
        "4":9,
        },
        "inventario":{}
},  

    28:{
        "frases":"Onde é o lugar natural mais baixo do planeta Terra ?\n\n Lago Baikal(1)\n Fossa das Marianas(2)\n Kidd Mine(3)\n Nehuma das alternativas(4)\n",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":8,
        "4":9,
        },
        "inventario":{}
},

    29:{
        "frases":"Qual idioma tem o maior número de palavras (de acordo com dicionários) ?\n\n Inglês(1)\n Português(2)\n Árabe(3)\n Japonẽs(4)\n ",
        "proximos_estados":{
        "1":8,
        "2":9,
        "3":9,
        "4":9,
        },
        "inventario":{}
},  

    30:{
        "frases":"Normalmente quantos litros de sangue uma pessoa tem, e quanto é retirado em uma doação de sangue ?\n\n De 4 a 6L, e são retirados 450ml(1)\n De 2 a 4L, e são retirados 450ml(2)\n De 4 a 6L, e são retirados 1L(3)\n De 2 a 4L, e são retirados 1L(4)\n",
        "proximos_estados":{
        "1":8,
        "2":9,
        "3":9,
        "4":9,
        },
        "inventario":{}
}, 

    31:{
        "frases":"De quem é a frase *penso logo existo* ?\n\n Platão(1)\n Sócrates(2)\n Galileu(3)\n Descartes(4)\n",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":9,
        "4":8,
        },
        "inventario":{}
}, 

    32:{
        "frases":"Onde foi inventado o chuveiro elétrico ?\n\n França(1)\n Suécia(2)\n Brasil(3)\n Itália(4)\n",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":8,
        "4":9,
        },
        "inventario":{}
},

    33:{
        "frases":"Qual o livro mais vendido do mundo após a bíblia ?\n\n Dom Quixote(1)\n Senhor dos Anéis(2)\n O Pequeno Príncipe(3)\n Ela, a feiticeira(4)\n",
        "proximos_estados":{
        "1":8,
        "2":9,
        "3":9,
        "4":9,
        },
        "inventario":{}
},  

    34:{
        "frases":"Atualmente quantos elementos químicos a tabela periódica possui ?\n\n 99(1)\n 108(2)\n 106(3)\n 118(4)\n",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":9,
        "4":8,
        },
        "inventario":{}
},

    35:{
        "frases":"Quais os países que têm a maior e a menor expectativa de vida do mundo ?\n\n Japão e Serra Leoa(1)\n Austrália e Afeganistão(2)\n Itália e Chade(3)\n Brasil e Congo(4)\n",
        "proximos_estados":{
        "1":8,
        "2":9,
        "3":9,
        "4":9,
        },
        "inventario":{}
},  

    36:{
        "frases":"Quais as duas datas que são comemoradas em novembro ?\n\n Independência do Brasil e Dia da Bandeira(1)\n Proclamação da República e Dia Nacional da Consciência Negra(2)\n Dia do Médico e Dia de São Lucas(3)\n Dia de Finados e Dia Nacional do Livro(4)\n",
        "proximos_estados":{
        "1":9,
        "2":8,
        "3":9,
        "4":9,
        },
        "inventario":{}
},

    37:{
        "frases":" Quanto tempo a luz do Sol demora para chegar à Terra ?\n\n 12 minutos(1)\n 1 dia(2)\n 12 horas(3)\n 8 minutos(4)\n",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":9,
        "4":8,
        },
        "inventario":{}
},

    38:{
        "frases":"Qual a velocidade da luz ?\n\n 300 000 000 metros por segundo (m/s)(1)\n 150 000 000 m/s(2)\n 199 792 458 m/s(3)\n 299 792 458 m/s(4)",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":9,
        "4":8,
        },
        "inventario":{}
},  

    39:{
        "frases":" Qual destes países é transcontinental ?\n\n Rússia(1)\n Filipinas(2)\n Marrocos(3)\n Groenlândia(4)\n",
        "proximos_estados":{
        "1":8,
        "2":9,
        "3":9,
        "4":9,
        },
        "inventario":{}
},
    40:{
        "frases":" Qual a melhor qualidade do Davi?\n\n Sua inteligência(1)\n Sua força(2)\n Sua beleza(3)\n Todos os anteriores(4)\n",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":9,
        "4":8,
        },
        "inventario":{}
},
    41:{
        "frases":" Você concorda que as vezes as pessoas são muito rudes sem motivo nenhum? Ontém na fila do pão eu tava esperando pra pegar meu pão de trigo né um pão bem quentinho prum ótimo café da tarde mas de repente o cara só chega e passa na minha frente nem pega senha e a moça atende ele ao invés de mim que peguei o papelzinho e fiquei esperando cara pqq tem pessoas que são assim detalhe ele ainda esbarrou em mim nem pra pedir desculpa credo\n\n Sim(1)\n Claro(2)\n Falou tudo(3)\n Se fosse eu dava logo um socão(4)\n",
        "proximos_estados":{
        "1":8,
        "2":8,
        "3":8,
        "4":8,
        },
        "inventario":{}
},
    42:{
        "frases":" Coringa! (deu azar)\n\n que saco...(1)",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":9,
        "4":9,
        },
        "inventario":{}
},
    43:{
        "frases":"...\n\n Biscoito(1)\n Bolacha(2)",
        "proximos_estados":{
        "1":9,
        "2":8,
        },
        "inventario":{}
},
    44:{
        "frases":" Aí você está numa aula de administração de redes e fez praticamente o trabalho todo nas duas últimas semanas kkkkkk.\n\n Bora(1)\n Vamo trabalhar(2)",
        "proximos_estados":{
        "1":8,
        "2":8,
        },
        "inventario":{}
},
    45:{
        "frases":" Will Smith levanta um estranho objeto prateado e põe um par de óculos escuros.\n\n Cobrir os olhos(1)\n O que?(2)",
        "proximos_estados":{
        "1":8,
        "2":9,
        },
        "inventario":{}
},
    46:{
        "frases":" O cartão do ônibus deu pau e você não tem dinheiro para pagar a passagem.\n\n Lamentar sua posição socioeconômica(1)\n Sair do ônibus(2)\n Pedir dinheiro emprestado do seu amigo(3)\n Brigar com o motorista(4)",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":8,
        "4":9,
        },
        "inventario":{}
},
    47:{
        "frases":" Qual país votou CONTRA a consideração de comida como um direito humano?\n\n Nigéria(1)\n Geórgia(2)\n Estados Unidos(3)\n Tunísia(4)",
        "proximos_estados":{
        "1":9,
        "2":9,
        "3":8,
        "4":9,
        },
        "inventario":{}
},


    4000:{
        'frases':'Digite "recomeçar" para limpar seu progresso e jogar de novo ou "1" Para receber seu Prêmio',
        "proximos_estados": {
        "1":4001,
        },
        "inventario":{}
},
    4001:{
        'frases':"colocar algo legal aqui depois" ,
        'proximos_estados':{},
        "inventario":{}
},


}   

#Tutorial
canais_de_voz = {}