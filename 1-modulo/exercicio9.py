"""
Escreva uma função Python que receba uma string
e conte o número de letras maiúsculas e minúsculas desta string.
"""
frase = str(input("Digite uma frase com maiúsculas e minusculas:\n"))
maiusculas = 0
minusculas = 0
for i in frase:
    if i == " ":
        continue
    elif i.upper() == i:
        maiusculas += 1 
    else:
        minusculas += 1 
print(f"A frase contem {maiusculas} maiusculas e {minusculas} minusculas")


"""
def check_char(text):
    type={"Uppercase":0, "Lowercase":0}
    for char in text:
        if char.isupper():
           type["Uppercase"]+=1
        elif char.islower():
           type["Lowercase"]+=1
    print ("Texto original: ", text)
    print ("Número de letras maiúsculas: ", type["Uppercase"])
    print ("Número de letras minúsculas: ", type["Lowercase"])

#string_test('The quick Brown Fox')
check_char("A melhor forma de prever o futuro é Criá-Lo")
"""
       
       
