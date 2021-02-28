print('=-='*4,'Desafio020','=-='*4)
o1 = str(input('Nome do primeiro aluno:'))
o2 = str(input('Nome do segundo aluno:'))
o3 = str(input('Nome do terceito aluno:'))
o4 = str(input('Nome do quarto aluno:'))
lista = [o1, o2, o3, o4]
from random import sample
sorte = sample(lista,4)
print(sorte)