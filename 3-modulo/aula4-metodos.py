class Filme:
    def __init__(self, nome, anoLancamento, inclusoPlano, nota, duracaoMinutos):
        self.nome = nome
        self.anoLancamento = anoLancamento
        self.inclusoPlano = inclusoPlano
        self.nota = nota
        self.duracaoMinutos = duracaoMinutos
        
    def __str__(self):
        return f"Filme: {self.nome}"
    
    def technical_sheet(self):
        print("####Dados do Filme####")
        print(f"Nome Filme: {self.nome}")
        print(f"Ano Lançamento: {self.anoLancamento}")
        print(f"Está no plano? {self.inclusoPlano}")
        print(f"Avaliação Filme: {self.nota}")
        print(f"Duração Filme: {self.duracaoMinutos}\n")

filme = Filme("Super Mario Bross", 2023, False, 5.0, 130)
filme2 = Filme("Avatar", 2025, False, 4.5, 220)
filme.technical_sheet()
filme2.technical_sheet()
