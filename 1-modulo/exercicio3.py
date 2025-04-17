"""
Substituindo caractere repetido
Escreva um programa Python para obter uma string de uma determinada string 
em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', 
exceto o próprio primeiro caractere
Ex:
fifa 23 → fi#a 23
restart→ resta#t
"""
nomeJogo      = "Fifa 23" 
primeiraLetra = nomeJogo[0].lower()
novoNome      = nomeJogo.replace(primeiraLetra, '$')
novoJogo      = primeiraLetra + novoNome[1:]
print(novoJogo)



