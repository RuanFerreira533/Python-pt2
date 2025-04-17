gameSet = {"Resident Evil 4", "Fifa 23", "Free Fire", "Valorant", "Counter Strike Global Ofensive"}
print(gameSet)

#Não possibilita recuperar valores via fatiamento ou slice

#1 buscar tamanho do Set
print(len(gameSet))

#2 True e 1 são considerados os mesmo valores
exemploTest = {"Fifa 23", True, 1, 90.50}
print(exemploTest)

#3 Adicionar itme de outro set
gameSet.update(exemploTest)
print(gameSet)

#4 Removendo item do Set
gameSet.remove(True)
gameSet.remove(90.50)
print(gameSet)