import re
 
text = 'OneBitCode: Transformamos pessoas em programadores sem limites'

# 1 - Índice inical e final de palavras
#O r significa que estamos trabalhando com uma string bruta (raw string) 
match = re.search(r'pessoas em programadores', text)
print('Índice inicial:', match.start())
print('Índice final:', match.end())

# 2 - Índice que tem o ponto
site = 'https://onebitcode.com/'
match = re.search(r'\.',site)
print(match)