class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    # Aplicando o Encapsulamento    
        #self.__salary = salary
    def show(self):
        # accessing public data member
        print(f"Nome: {self.name} Salário: {self.salary}")
        
fulano = Employee("Fulano", 1000)
sicrano = Employee("Sicrano", 10000)
fulano.name = "Fulano 2"
fulano.salary = 40000
fulano.show()
sicrano.show()