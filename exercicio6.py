"""
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
Para salários superiores a R$ 1.250,00, 
calcule um aumento de 10%. 
Para os inferiores ou iguais, de 15%.
"""
salario = float(input("Digite seu salário: "))
porcentagemAumento = 0.15

if salario > 1250:
    porcentagemAumento = 0.10
aumento = salario * porcentagemAumento

print(f"Seu aumento será de: R$ {aumento:.2f}")