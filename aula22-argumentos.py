# 1 crie uma função que recebe o primeiro nome e o ultimo nome
def nome_completo(fname, lname):
   print(f"Nome completo: {fname} {lname}")
   
nome_completo("Ruan", "Silva")

#
def soma(a, b):
    print(a + b)
soma(20, 10)
#
def endereco(country="Brasil"):
    print(f"Eu moro no {country}")
endereco()
endereco("Canadá")
#
def nota_jogo(qtd):
    nomeJogo = input("Digite o nome do jogo\n")
    soma = 0
    for i in range(qtd):
        nota = float(input("Digite a nota para o jogo \n"))
        soma += nota
    print(f"Média de avaliação do jogo {nomeJogo} é: {soma/qtd}")

qtd = int(input("Digite quantas avaliações deseja fazer no jogo\n"))
nota_jogo(qtd)
