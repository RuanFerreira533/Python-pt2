"""
*args: Utilizamos ele quando não temos a certeza de quantos
argumentos vamos ter dentro de uma função. Ao utilizá-lo, 
deixamos essa informação dinâmica e variável.
- Os argumentos são passados como uma tupla.

**kwargs: Além dos valores, podemos passar também as respectivas
chaves para cada argumento.
- Os argumentos são passados como um dicionário.
"""
def soma(*num):
    soma_total = 0
    
    for n in num:
        soma_total = soma_total + n

    print(f"Soma é: {soma_total}")
soma(7)
soma(8, 7)
soma(4, 5, 9)
soma(6, 8, 3, 1)

def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("######Curso######")
presentation(nome="Python", categoria="Backend", level="Iniciante")