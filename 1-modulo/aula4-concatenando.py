nome    = input("Qual o seu nome?\n")
idade   = int( input("Qual sua idade?\n"))
salario = float( input("Quanto você recebe?\n"))
sexo    = input("Qual seu sexo?\n")

print("==============")
print("Alternativa 01")
print("Dados pessoais")
print("==============")

print("Nome: "   , nome)
print("Idade: "  , idade)
print("Salario: ", salario)
print("Sexo "    , sexo)

#Alternativa 2#
print("==============")
print("Alternativa 02")
print("==============")

print (" Nome:", nome, 
       "\n Idade: ", idade, 
       "\n Salário: ",  salario, 
       "\n Sexo: ", sexo
      )

#Alternativa 3#
print("==============")
print("Alternativa 03")
print("==============")

print(f"Nome: {nome} \nIdade: {idade} \nSalário: {salario} \nSexo: {sexo}") 
