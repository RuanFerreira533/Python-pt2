gameList = ["Resident Evil 4", "Fifa 23", "Free Fire", "Valorant", "Counter Strike Global Ofensive"]

#Tamanho da lista
print(len(gameList))

#Recuperando item da lista pelo indice
print(gameList.index("Valorant"))

#Adicionando item no final da lista
gameList.append("GTA V")
print(gameList)

#Ordenando lista em ordem alfabética
gameList.sort()
print(gameList)

#Copiando uma lista para outra
nemGameList = gameList.copy()
nemGameList.remove("Valorant")
print(nemGameList)

#Remove todos os itens da lista
gameList.clear()
print(gameList)