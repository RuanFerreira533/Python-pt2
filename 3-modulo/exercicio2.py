"""
Desenvolva uma classe em Python para atender as seguintes especificidades de um Produto:

1 - Cada produto deve ter um preço e um nome.
2 - A classe deve ter um método construtor e o método dundle str.
3 - A classe deve ter um método para desconto. 
O método deve receber o desconto em percentual e realizar o 
cálculo de quanto ficaria o preço final com o desconto.

"""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome} - R$ {self.preco} reais"

    def desconto(self, desconto):
        valorDesconto = (self.preco/100) * desconto
        precoFinal = self.preco - valorDesconto
        return int(precoFinal)
    
xbox = Produto("Xbox One", 4000)
print(xbox)
print(xbox.desconto(20))
iphone = Produto("Iphone 14", 8000)
print(iphone)
print(iphone.desconto(10))