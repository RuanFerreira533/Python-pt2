#Lista de valores de 1 a 10 menores que 4 
#for i in (range(10)):
#   if i < 4:
#       print(i)

listNumeros = [i for i in range(10) if i < 4]
print(listNumeros)
#
gameList = ["Resident Evil 4", "Fifa 23", "Free Fire", "Valorant", "Counter Strike Global Ofensive"]
#Jogos que possuem a letra A
novaLista = [x for x in gameList if "a" in x ]
print(novaLista)

#Todos os jogos menos Fifa 23
novaLista = [x for x in gameList if x != "Fifa 23" ]
print(novaLista)
