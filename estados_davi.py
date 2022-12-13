estados = {
    
  #Tutorial
  
  0:{
        "frases":"Iniciar o jogo?\n\n SIM(1)\n NÃO(2)\n Pular Tutorial(3)", 
        "proximos_estados":{
            "1": 1,
            "2":2,
            "3":4000,
            "inventario":{}
            
        }
},
    1:{
    "frases":"Bem vindo cidadão, este é um programa experimental desenvolvido pelo governo com o intuito de  ₦ ₧ ₨ ₪ ₫ € ₭ ₮ ₯\n\n Iremos te fazer algumas perguntas.\n\n Prosseguir(1). ",
    "proximos_estados":{
        "1":3,
        "inventario":{}
        }
},
    2:{
        "frases":"Desconectando.",
        "proximos_estados":{
        "inventario":{}
        
    }
        
},
    3:{
        "frases":'Como você ouviu falar do nosso programa?\n\n Notícias(1)\n No Zap(2)',
        "proximos_estados":{
        "1":4,
        "2":5,
        "inventario":{}
        }
  
},
    4:{
      
      "frases":"Como você dorme?\n\nDe ladinho(1)\n\nBarriga pra cima(2)",
      "proximos_estados":{
        "1":5,
        "2":5,
        "inventario":{}
      }
},
    5:{
      
      "frases":"Como você dorme?\n\nDe ladinho(1)\n\nBarriga pra cima(2)",
      "proximos_estados":{
        "1":6,
        "2":6,
        
        "inventario":{}
      }
      
},
    6:{
      
      "frases":"Nenhuma das suas escolhas até agora importaram, era só pra você se acostumar com o jogo, agora o jogo começa.\n\nProsseguir(1)\nChorar(2)",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
# Fim do tutorial      
},



#Estados especiais de acerto e derrota
  
    8:{
      "frases":"",
      "proximos_estados":{
      "1":4000
      }
},
    9:{
      "frases":"",
      "proximos_estados":{
        "1":4000
      }

},

  


#estados do GAME
  
    10:{
      
      "frases":"quantas asas tem um pássaro\n\n Duas(1)\n cinquenta(2)\n",
      "proximos_estados":{
        "1":8,
        "2":9,
        
        "inventario":{}
      }
      
},
    11:{
      
      "frases":"Quantos braços saudáveis o enzo tem\n\n Um(1)\n Dois(2)\n",
      "proximos_estados":{
        "1":8,
        "2":9,
        
        "inventario":{}
      }
      
},  
    12:{
      
      "frases":"Qual a cor do céu?\n\n Cinza(1)\n Azul(2)\n",
      "proximos_estados":{
        "1":9,
        "2":8,
        
        "inventario":{}
      }
      
},
    13:{
      
      "frases":"Quantos tijolos tem o Ifsc?\n\n Varios mano(1)\n Nenhum(2)\n",
      "proximos_estados":{
        "1":8,
        "2":9,
        
        "inventario":{}
      }
      
},  
    14:{
      
      "frases":"Qual o nome\n\n Biscoito(1)\n Bolacha(2)\n",
      "proximos_estados":{
        "1":9,
        "2":8,
        
        "inventario":{}
      }
      
},
    15:{
      
      "frases":"O que você merece\n\n Nada(1)\n Tudo(2)\n",
      "proximos_estados":{
        "1":8,
        "2":9,
        
        "inventario":{}
      }
      
},
    16:{
      
      "frases":"16",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    17:{
      
      "frases":"17",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    18:{
      
      "frases":"18",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    19:{
      
      "frases":"19",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
}, 
    20:{
      
      "frases":"20",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
}, 
    21:{
      
      "frases":"21",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    22:{
      
      "frases":"22",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    23:{
      
      "frases":"23",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    24:{
      
      "frases":"24",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    25:{
      
      "frases":"25",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    26:{
      
      "frases":"26",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    27:{
      
      "frases":"27",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    28:{
      
      "frases":"28",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    29:{
      
      "frases":"29",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    30:{
      
      "frases":"30",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
}, 
    31:{
      
      "frases":"31",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
}, 
    32:{
      
      "frases":"10",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    33:{
      
      "frases":"11",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    34:{
      
      "frases":"12",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    35:{
      
      "frases":"13",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    36:{
      
      "frases":"14",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    37:{
      
      "frases":"15",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    38:{
      
      "frases":"16",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    39:{
      
      "frases":"17",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    40:{
      
      "frases":"18",estados = {
    
  #Tutorial
  
  0:{
        "frases":"Iniciar o jogo?\n\n SIM(1)\n NÃO(2)\n Pular Tutorial(3)", 
        "proximos_estados":{
            "1": 1,
            "2":2,
            "3":4000,
            "inventario":{}
            
        }
},
    1:{
    "frases":"Bem vindo cidadão, este é um programa experimental desenvolvido pelo governo com o intuito de  ₦ ₧ ₨ ₪ ₫ € ₭ ₮ ₯\n\n Iremos te fazer algumas perguntas.\n\n Prosseguir(1). ",
    "proximos_estados":{
        "1":3,
        "inventario":{}
        }
},
    2:{
        "frases":"Desconectando.",
        "proximos_estados":{
        "inventario":{}
        
    }
        
},
    3:{
        "frases":'Como você ouviu falar do nosso programa?\n\n Notícias(1)\n No Zap(2)',
        "proximos_estados":{
        "1":4,
        "2":5,
        "inventario":{}
        }
  
},
    4:{
      
      "frases":"Como você dorme?\n\nDe ladinho(1)\n\nBarriga pra cima(2)",
      "proximos_estados":{
        "1":5,
        "2":5,
        "inventario":{}
      }
},
    5:{
      
      "frases":"Como você dorme?\n\nDe ladinho(1)\n\nBarriga pra cima(2)",
      "proximos_estados":{
        "1":6,
        "2":6,
        
        "inventario":{}
      }
      
},
    6:{
      
      "frases":"Nenhuma das suas escolhas até agora importaram, era só pra você se acostumar com o jogo, agora o jogo começa.\n\nProsseguir(1)\nChorar(2)",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
# Fim do tutorial      
},



#Estados especiais de acerto e derrota
  
    8:{
      "frases":"",
      "proximos_estados":{
      "1":4000
      }
},
    9:{
      "frases":"",
      "proximos_estados":{
        "1":4000
      }

},

  


#estados do GAME
  
    10:{
      
      "frases":"quantas asas tem um pássaro\n\n Duas(1)\n cinquenta(2)\n",
      "proximos_estados":{
        "1":8,
        "2":9,
        
        "inventario":{}
      }
      
},
    11:{
      
      "frases":"Quantos braços saudáveis o enzo tem\n\n Um(1)\n Dois(2)\n",
      "proximos_estados":{
        "1":8,
        "2":9,
        
        "inventario":{}
      }
      
},  
    12:{
      
      "frases":"Qual a cor do céu?\n\n Cinza(1)\n Azul(2)\n",
      "proximos_estados":{
        "1":9,
        "2":8,
        
        "inventario":{}
      }
      
},
    13:{
      
      "frases":"Quantos tijolos tem o Ifsc?\n\n Varios mano(1)\n Nenhum(2)\n",
      "proximos_estados":{
        "1":8,
        "2":9,
        
        "inventario":{}
      }
      
},  
    14:{
      
      "frases":"Qual o nome\n\n Biscoito(1)\n Bolacha(2)\n",
      "proximos_estados":{
        "1":9,
        "2":8,
        
        "inventario":{}
      }
      
},
    15:{
      
      "frases":"O que você merece\n\n Nada(1)\n Tudo(2)\n",
      "proximos_estados":{
        "1":8,
        "2":9,
        
        "inventario":{}
      }
      
},
    16:{
      
      "frases":"16",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    17:{
      
      "frases":"17",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    18:{
      
      "frases":"18",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    19:{
      
      "frases":"19",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
}, 
    20:{
      
      "frases":"20",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
}, 
    21:{
      
      "frases":"21",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    22:{
      
      "frases":"22",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    23:{
      
      "frases":"23",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    24:{
      
      "frases":"24",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    25:{
      
      "frases":"25",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    26:{
      
      "frases":"26",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    27:{
      
      "frases":"27",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    28:{
      
      "frases":"28",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    29:{
      
      "frases":"29",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    30:{
      
      "frases":"30",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
}, 
    31:{
      
      "frases":"31",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
}, 
    32:{
      
      "frases":"10",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    33:{
      
      "frases":"11",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    34:{
      
      "frases":"12",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    35:{
      
      "frases":"13",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    36:{
      
      "frases":"14",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    37:{
      
      "frases":"15",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    38:{
      
      "frases":"16",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    39:{
      
      "frases":"17",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},
    40:{
      
      "frases":"18",
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    






  
}
partidas = {}
canais_de_voz = {}
      "proximos_estados":{
        "1":4000,
        "2":4000,
        
        "inventario":{}
      }
      
},  
    



}
partidas = {}
canais_de_voz = {}