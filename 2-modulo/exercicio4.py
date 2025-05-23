"""
Escreva um programa em Python que gera um número aleatório para que o usuário 
tente acertar o número. Algumas sugestões para o programa:

1 - Utilizar um laço de repetição para que o programa execute até 
que o usuário informe um número referente a opção para sair do programa.

2 - Utilizar o módulo random para gerar valores aleatórios dentro de um intervalo. 
Ex: 1 a 10.

3 - Lê o número que o usuário digitar via input e comparar 
se é o mesmo número que o programa sorteou.
"""
import random

numero = 1
while numero == 0:
    print("Jogo da adivinhação")
    numero = int(input("Digite um numero de 1 á 10: "))
    resultado = random.randint(1, 10)
    if numero == resultado:
        print("Parabéns você acertou o resultado!")
        numero = 0   
    else:
        print(f"Você errou, o resultado era: {resultado}") 
        