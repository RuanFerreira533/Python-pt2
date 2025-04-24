from collections import Counter, namedtuple, deque
from operator import itemgetter
 
#1 - Contar itens de uma lista
listaFrutas = ["Maçã", "Banana", "Laranja", "Limão", "Maçã"]
print(listaFrutas)
print(Counter(listaFrutas))

#2 - Tuplas domeada
jogo = namedtuple('jogo', ['nome', 'preco', 'nota'])
j1 = jogo("Fifa 23", 90.50, 8.5)
j2 = jogo("Resident Evil 4", 300.00, 10.0)
print(j1)
print(j2)

#3- Ordenando Dicionarios
alunos = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}
a = sorted(alunos.items(), key=itemgetter(0))
print(alunos)
print(a)

#4- Fila com ambas extremidades
deq = deque([20,40,60,80])
deq.appendleft(10)
print(deq)
deq.append(90)
deq.popleft()
deq.pop()
print(deq)