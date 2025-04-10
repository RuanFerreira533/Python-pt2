import pprint
games = {
    "fifa 23"  : {
                  "ano": 2022,
                  "preco": 90.50,
                  "classificao":8.5,
                  "genero": ["esporte", "familia"]
                 },

    "free fire": {
                  "ano": 2020,
                  "preco": 00.00,
                  "classificao":8.5,
                  "genero": ["battle royale", "tiro"]
                 },
    "valorant" : {
                  "ano": 2023,
                  "preco": 00.00,
                  "classificao":7.0,
                  "genero":["bomba", "tiro"]
                 }
    }
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(games)

#Buscar informação
print(games["valorant"] ["genero"])

#Adicionar Item
games["valorant"]["players"] = 10
print(games["valorant"])

#Remover dicionario
del games ["valorant"]
pp.pprint(games)
