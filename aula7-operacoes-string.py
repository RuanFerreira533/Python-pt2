nomeJogo  = "Fifa 25"
descricaoJogo = """
Fifa 25 jogo de futebol lançado em 2025
Produzido pela EA Sports
"""

#String:[ inicio:fim ] indice final - 1

print(descricaoJogo[0:8])#Fifa 25
print(descricaoJogo[6:8])#25

#Des da primeira posição
print(descricaoJogo[0:])#Fifa 25 jogo de futebol lançado em 2025
#Até a ultima posição
print(descricaoJogo[:4])#Fif

"""
string[início:fim:passo] - índice começa com 0 | índice final -1 | 
passo - determina o incremento. Por padrão esse número é o 1
"""
#De 2 em 2 caracteres
print(descricaoJogo[::2])

#Indice impares
print(descricaoJogo[1::2])

#invertendo a string
print(descricaoJogo[::-1])