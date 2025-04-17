"""
Escreva um módulo em python para tratar algumas strings e 
que possua as seguintes funcionalidades:

1-Inverter uma string de trás pra frente.
2-Retornar apenas letras com índice par.
3-Retornar apenas letras com índice ímpar.
"""
import strings

print(strings.inv(input("Digite uma palavra para ser invertida: \n")))

print(strings.imp(input("Digite uma palavra para retornar ops indices impares: \n")))

print(strings.par(input("Digite uma palavra para retornar ops indices pares: \n")))