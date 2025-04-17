"""
Adicionar um time
Remover um time
Listar times
Adicionar jogador em um time
Remover jogador de um time
Listar jogadores de um time
"""
import pprint
pp = pprint.PrettyPrinter(depth=4)
acao = 0
times = {
    "Paris Saint German": 
        {
        "Jogadores": [],
        "Região"   : "França",
        },

    "Real Madrid":  
        {
        "Jogadores": [],
        "Região"   : "Espanha",
        },
    "Barcelona" : 
        {
        "Jogadores": ["Ruan"],
        "Região"   : "Espanha",
        },
    }
while acao != 9:
    print("1 - Adicionar um time")
    print("2 - Remover um time")
    print("3 - Listar times")
    print("4 - Adicionar um jogador")
    print("5 - Remover um jogador")
    print("6 - Listar jogadores de um time")
    print("9 - Sair")
    acao = int(input("Qual ação você deseja tomar?\n"))
    if acao == 1:
       novoTime      = input("Digite o nome do time que será cadastrado: \n")
       novoRegiao    = input("Digite o nome da região do time: \n")
       times[novoTime] ={
                        "Jogadores": [],
                        "Região"   : novoRegiao,
                        }
       pp.pprint(times)
    elif acao == 2:
       pp.pprint(times)
       removerTime = input("Digite o nome do time que será removido: \n")
       del times [removerTime]
       pp.pprint(times)
       
    elif acao == 3:
        pp.pprint(times)
    elif acao == 4:
        pp.pprint(times.keys())
        nomeTime = input("Digite o nome do time que será cadastrado o novo jogador: \n")
        if nomeTime in times:
            nomeJogador = input("Digite o nome do jogador que será cadastrado: \n")
            times[nomeTime]["Jogadores"].append(nomeJogador)
            print(nomeTime)
            pp.pprint(times[nomeTime])
        else:
           print("Time não encontrado")
    elif acao == 5:
        pp.pprint(times.keys())
        nomeTime = input("Digite o nome do time que será removido o novo jogador: \n")
        if nomeTime in times:
            nomeJogador = input("Digite o nome do jogador que será removido: \n")
            if nomeJogador in times[nomeTime]["Jogadores"]:
               times[nomeTime]["Jogadores"].remove(nomeJogador)
               print(nomeTime)
               pp.pprint(times[nomeTime])
            else:
               print("Jogador não encontrado")
        else:
           print("Time não encontrado")
    elif acao == 6:
        pp.pprint(times.keys())
        nomeTime = input("Digite o nome do time que será listado os jogadores: \n")
        if nomeTime in times:
           pp.pprint(times[nomeTime]["Jogadores"])
        else:
           print("Time não encontrado")
    