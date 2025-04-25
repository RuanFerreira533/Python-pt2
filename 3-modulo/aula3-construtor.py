class Filme:
    def __init__(self, nome, anoLancamento, inclusoPlano, nota, duracaoMinutos):
        self.nome = nome
        self.anoLancamento = anoLancamento
        self.inclusoPlano = inclusoPlano
        self.nota = nota
        self.duracaoMinutos = duracaoMinutos
        
    def __str__(self):
        return f"Filme: {self.nome}"

filme = Filme("Super Mario Bross", 2023, False, 5.0, 130)
filme2 = Filme("Avatar", 2025, False, 4.5, 220)
print(filme.nome)
print(filme.nota)
print(filme2.nome)
print(filme2.nota)
print(filme2)