"""
Escreva uma função Python para imprimir os números pares e ímpares
em duas listas separadas para cada uma.
"""
impar   = 0
par     = 0
numeros = 0
listaPares = []
listaImpares = []
while(numeros != -1):
    numeros = int(input("Digite o número:\n"))
    if(numeros != -1):
        if numeros % 2 == 0:
           par += 1
           listaPares.append(numeros)
        elif numeros % 2 == 1:
           impar += 1
           listaImpares.append(numeros)
print(f"Na lista tem {impar} impares são eles {listaImpares} e {par} pares são eles {listaPares}")

"""
def check_numbers(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return pairs, odd
print(check_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
"""