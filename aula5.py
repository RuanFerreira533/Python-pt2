num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

sum  = num1 + num2 #Soma
sub  = num1 - num2 #Subtração
div  = num1 / num2 #Divisão
mult = num1 * num2 #Multiplicação
mod  = num1 % num2 #Resto da divisão
exp  = num1 ** num2 #exponenciação
print("==========")
print(f"Soma dos números é: {sum} \nSubtração dos números é: {sub} \nDivisão dos números é: {div} \nMultiplicação dos número é {mult} \nA sobra da divisão é: {mod} \nA exponenciação dos números é: {exp}")

maior       = num1 > num2
menor       = num1 < num2
igual       = num1 == num2
diferente   = num1 != num2 
maior_igual = num1 >= num2
menor_igual = num1 <= num2

print("==========")
print(f"O número {num1} é maior que {num2} ? {maior}")
print(f"O número {num1} é menor que {num2} ? {menor}")
print(f"Os números {num1} e {num2} são iguais? {igual}")
print(f"Os números {num1} e {num2} são diferentes? {diferente}")
print(f"Os números {num1} e {num2} são maiores ou iguais? {maior_igual}")
print(f"Os números {num1} e {num2} são menores ou iguais? {menor_igual}")

#Atribuição
num1 += 1 # num1 = num1 + 1 
