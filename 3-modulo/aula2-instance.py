class Filme:
    nome = ""
    anoLancamento = 0
    inclusoPlano  = False
    nota = 0
    duracaoMinutos = 0
    
# Primeiro Filme #
filme = Filme()
filme.nome = "Super Mario Bross"
filme.anoLancamento = 2023
filme.inclusoPlano = False
filme.nota = 5.0
filme.duracaoMinutos = 130
print("Dados do filme")
print(f"Nome do filme: {filme.nome} \nAno de lançamento: {filme.anoLancamento}" )
