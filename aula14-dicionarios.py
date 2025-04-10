#Dicionarios
gameFifa = {
    "name": "Fifa 23",
    "ano": 2022,
    "preco": 90.50,
    "classificao":8.5,
    "genero": ["esporte", "familia"]
}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

#Recuperar elemento do dicionario
print(gameFifa["genero"])
print(gameFifa.get("classificao"))

#Apenas chaves do dicionario
print(gameFifa.keys())

#Apenas os valores
print(gameFifa.values())

#Buscar chave e valor
print(gameFifa.items())

#Adicionar itens no dicionario
gameFifa["players"] = 2
print(gameFifa)

#Alterando dicionario
gameFifa["players"] = 3
print(gameFifa)

#Remover item
gameFifa.pop("players")
print(gameFifa)