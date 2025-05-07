class Animal:
    nome = ""
    tamanho = ""
    cor = ""
    
    def eat(self):
        print("Animal se alimentando")
        
class Cavalo(Animal):
    raca = ""
    
    def escape(self):
        print("Cavalo fugindo")
        
class Leao(Animal):
    mane = True
    
    def hunt(self):
        print("Leão caçando")
        
c = Cavalo()
c.nome = "Pé de pano"
c.cor  = "Branco"
c.escape()
c.eat()

l = Leao()
l.nome = "Simba"
l.cor  = "Marrom"
l.hunt()
l.eat()


        