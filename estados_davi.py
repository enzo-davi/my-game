estados = {
    0:{
        "frases":"Iniciar o jogo?\n\n SIM(1)\n NÃO(2)", 
        "proximos_estados":{
            "1": 1,
            "2":2,
            "inventario": {"chave_dourada", "chave_prateada"}
            
        }
},
    1:{
    "frases":"Bem vindo cidadão, este é um programa experimental desenvolvido pelo governo com o intuito de  ₦ ₧ ₨ ₪ ₫ € ₭ ₮ ₯\n\ Iremos te fazer algumas perguntas:\n\n Prosseguir(1). ",
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
        
}

}

partidas = {}

# estados[estado_do_jogador]["frases"]