print('=-='*10)
print(' VAMOS JOGAR PAR OU IMPAR!')
print('=-='*10)
from random import randint
a = ''
win = 0
while True:
    ale = randint(1, 10)
    v = int(input(' Digite um valor: '))
    j = str(input(' Par ou Impar? [I/P]: ')).strip().upper()[0]
    r = ale + v
    if r % 2 == 0:
        a = 'P'
    else:
        a = 'I'
    if j == a:
        win += 1
        print('=-=' * 10)
        print('Você venceu, vamos de novo!')
        print(f'O computador escolheu o número {ale}')
        print('=-=' * 10)
    else:
        print('=-=' * 10)
        print('Você perdeu!')
        print(f'O computador escolheu o número {ale}')
        print('=-=' * 10)
        break
if win > 0:
    print(f'Você venceu {win} partida(s).')




