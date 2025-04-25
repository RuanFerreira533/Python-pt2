class Filme:
    def __init__(self, nome, anoLancamento, inclusoPlano, nota, avaliadores, duracaoMinutos):
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

filme = Filme("Super Mario Bross", 2023, False, 0.0, 0.0, 130)

nota = 0
avaliadores = 0
acao = 0

while acao == -1:
    nota == input(f"Digite uma nota de 0 a 5 para o filme e -1 para parar {filme.nome} ")
    avaliadores += 1
    acao == input(f"Deseja continuar?")
    

media = nota / avaliadores
Filme("Super Mario Bross", 2023, False, media , avaliadores, 130)