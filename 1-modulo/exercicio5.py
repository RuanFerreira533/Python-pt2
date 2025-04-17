"""
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, 
e R$ 0,35 para viagens mais longas.
"""

distancia = int(input("Qual será a distancia percorrida(KM) ? "))
#
if distancia <= 200:
   valor = distancia * 0.50
else:
   valor = distancia * 0.35
#
print(f"Sera cobrado um valor de R${valor} pela viagem")
