from random import randint
from time import sleep
lista = []
pares = []


def sortea():
    for cont in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        cont += 1
    print(f'Sorteando 5 valores da lista:', end=' ')
    for n in lista:
        sleep(0.3)
        print(f'{n}', end=' ')
    print('Pronto!')


def somandopar():
    r = 0
    for p in lista:
        if p % 2 == 0:
            r += p
    print(f'Somando os valores pares de {lista}, temos {r}.')


sortea()
somandopar()