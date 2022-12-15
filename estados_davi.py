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
      
      "frases":"Quantas copas tem o Brazil ?\n\n 4(1)\n 5(2)\n 6(3)\n Nenhuma(4)\n",
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
        "frases":"Qual a capital da Croácia ?\n\n Zagrebe(1)\n Berlim(2)\n Saravejo(3)\n Belgrado(4)",
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
        "1":9,
        "2":9,
        "3":9,
        "4":8,
        },
        "inventario":{}
},

    18:{
      
      "frases":"18",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},  
    19:{
      
      "frases":"19",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
}, 
    20:{
      
      "frases":"20",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
}, 
    21:{
      
      "frases":"21",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},
    22:{
      
      "frases":"22",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},  
    23:{
      
      "frases":"23",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},
    24:{
      
      "frases":"24",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},  
    25:{
      
      "frases":"25",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},
    26:{
      
      "frases":"26",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},
    27:{
      
      "frases":"27",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},  
    28:{
      
      "frases":"28",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},
    29:{
      
      "frases":"29",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},  
    30:{
      
      "frases":"30",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
}, 
    31:{
      
      "frases":"31",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
}, 
    32:{
      
      "frases":"10",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},
    33:{
      
      "frases":"11",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},  
    34:{
      
      "frases":"12",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},
    35:{
      
      "frases":"13",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},  
    36:{
      
      "frases":"14",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},
    37:{
      
      "frases":"15",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},
    38:{
      
      "frases":"16",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},  
    39:{
      
      "frases":"17",
      "proximos_estados":{
        "1":4000,
        "2":4000,
      },
        "inventario":{}
      
      
},

    4000:{
        "frases":"teste",
        "proximos_estados": {
          '1': 0
        },
        "inventario":{}
    
},
}   
    


  #Tutorial
canais_de_voz = {}