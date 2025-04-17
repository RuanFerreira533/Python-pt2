"""
Substituindo caractere repetido
Escreva um programa Python para obter uma única string de duas strings fornecidas, 
separadas por um espaço e troque os dois primeiros caracteres de cada string.

Ex:
abc xyz → xyc abz
"""

frase  = input('Digite 6 caracteres com um espaço entre os 3 primeiros e os 3 últimos: ')#abc xyz
primeiros = frase[0:2]#ab
sobraPrimeiros = frase[2:3]#c
ultimos   = frase[4:6]#xy
sobraUltimos = frase[6:7]#z
print (f"{ultimos}{sobraPrimeiros} {primeiros}{sobraUltimos}")

#Resolução
st1 = 'abc'
st2 = 'xyz'

new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]

print(f"{new_st1} {new_st2}")