"""
3 -> 3 * 2 * 1
5 -> 5 * 4 * 3 * 2 * 1
"""
def fatorial(num):
   if num == 1:
       return 1
   else:
      return (num * fatorial(num -1))
  
numero = int(input("Digite um número para fazer seu fatorial: \n"))
print(f"O fatorial de {numero} é {fatorial(numero)}") 

"""
3 -> 3 * 2 * 1
5 -> 5 * 4 * 3 * 2 * 1
"""
def soma(num):
   if num == 1:
       return 1
   else:
      return (num + soma(num -1))
  
numero = int(input("Digite um número para fazer sua soma: \n"))
print(f"A soma de {numero} é {soma(numero)}") 

