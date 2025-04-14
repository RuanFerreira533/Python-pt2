def helloWorld():
    print("Hello World")
    
helloWorld()
#
def soma():
    return(5 + 4)
    
print(soma())
#
def create_game():
    nome = input("Digite o nome do jogo \n")
    anolancamento = int(input("Digite o ano de lançamento\n"))
    precoJogo = float(input("Digite o preço do jogo\n"))
    notaJogo = float(input("Digite a nota de avaliação do jogo\n"))
    print(nome)
    print(anolancamento)
    print(precoJogo)
    print(notaJogo)
    
    print(f"{nome} - R$ {precoJogo}")
    
create_game()
