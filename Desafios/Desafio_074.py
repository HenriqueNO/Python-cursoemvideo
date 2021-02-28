from random import randint
a = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Eu sortiei os valores: ', end='')
menor = maior = 0
for c in a:
    print(f'{c}', end=' ')
print(f'\nO maior valor sorteado foi: {max(a)}')
print(f'O menor valor sorteado foi: {min(a)}')
