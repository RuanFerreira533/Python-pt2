#Faça um programa que calcule a tabuada de um número, 
# com valores iniciais e finais informados pelo usuário

numero = int(input("Digite o número de qual sera a tabuada\n"))
qtd    = int(input("até quantas vezes voce quer essa tabuada?\n"))

for i in range(qtd):
    resultado = numero * qtd
    print(f"{numero} x {qtd} = {resultado} ")  
    qtd += -1