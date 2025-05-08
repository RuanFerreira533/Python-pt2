"""
1 - Usuário deve informar o seu nome para cadastrar uma viagem.

2 - Usuário deve selecionar um destino com base nas instâncias de objetos da classe viagem.

3 - Deve ser apresentado uma mensagem indicando que o a cadastro da viagem no 
destino específico foi feito com sucesso.
"""
class Viagem:
    def __init__(self, destino):
        self.destino = destino
        
Viagem_0 = Viagem("Brasil")
Viagem_1 = Viagem("Argentina")
Viagem_2 = Viagem("Cuba")
Viagem_3 = Viagem("Colombia")
Viagem_4 = Viagem("Venezuela")

print("Ola, tudo bem? Temos alguma opções de viagens para você!")
nomePessoa = input("Digite seu nome para começarmos: ")
print(f"{nomePessoa} Temos 5 opções que combinam com você:"
'''
[0] Brasil
[1] Argentina
[2] Cuba
[3] Colombia
[4] Venezuela
'''      
) 
escolha =  int(input("Selecione o destino da viagem: "))
lista_viagem = [Viagem_0, Viagem_1, Viagem_2, Viagem_3, Viagem_4 ]

for opcoes in lista_viagem:
    if escolha >= 5:
        print("Está opção não está inclída em nosso planos.")
        break
    if escolha <= 4:
        print(f"{nomePessoa} sua viagem para {lista_viagem[escolha].destino} está marcada")
        print("Volte sempre")
        break