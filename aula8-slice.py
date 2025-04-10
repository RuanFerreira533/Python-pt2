nomeJogo  = "fiFa 25"
descricaoJogo = """
Fifa 25 jogo de futebol, lançado em 2025,
Produzido pela EA Sports
"""
#
print(nomeJogo.upper())#Maiusula FIFA 25
print(nomeJogo.lower())#Minuscula fifa 25
print(nomeJogo.capitalize())#1 Letra em maiuscula Fifa 25
print(nomeJogo.title())#Apenas a 1 Letra em maiúscula Fifa 25
print(nomeJogo.center(10, '-'))#Centraliza utilizando '-'  -fifa 25-- com 10 caracteres
print(descricaoJogo.find("a"))#Retorna a posição de um determinado caracter 4
print(descricaoJogo.count("f"))#Retorna a quantidade de caracteres "f" --minusculo --2
print(descricaoJogo.replace("Fifa",  "Pes"))#Altera um nome pelo outro
print(descricaoJogo.split(','))#Quebra a string em ','