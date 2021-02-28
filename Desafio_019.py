import random

print('=-='*4, 'Desafio019', '=-='*4)
a1 = str(input('Coloque o nome do aluno 1:'))
a2 = str(input('Coloque o nome do aluno 2:'))
a3 = str(input('Coloque o nome do aluno 3:'))
a4 = str(input('Coloque o nome do aluno 4:'))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O sortudo foi {}!'.format(escolhido))