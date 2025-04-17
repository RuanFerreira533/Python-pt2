gameName = input("Digite o nome do jogo\n")
qtdNota = 0
totalNota = 0
nota = 0
media = 0

while(nota != -1):
    nota = float(input("Digite a nota:\n"))
    if(nota != -1):
        totalNota += nota 
        qtdNota += 1
        media = totalNota / qtdNota
print(f"A média das notas do jogo {gameName} é {qtdNota:.2f}")