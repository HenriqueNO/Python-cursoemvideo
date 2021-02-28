print(' [ 0 ] pedra\n [ 1 ] Tesoura\n [ 2 ] papel ')
res = int(input('Digite um numero correspondente ao jogo: '))
from random import randint
iten = ('pedra', 'papel', 'tesoura', '?','?','?')
pc = randint(0,2)
print('Computador jogou {}'.format(iten[pc]))
print('Jogador jogou {}'.format(iten[res]))
print('\033[1;36m=-<>-=\033[m'*3)
if pc == 0: # computador jogou PEDRA
    if res == 0:
        print('\033[1;33m Empate!')
    elif res == 1:
        print('\033[1;31m Computador vence!')
    elif res == 2:
        print('\033[1;34m Jogador vence!')
    else:
        print('\033[1;31m Jogada Invalida!')
if pc == 1: # computador jogou TESOURA
    if res == 0:
        print('\033[1;34m Jogador vence!')
    elif res == 1:
        print('\033[1;33m Empate!')
    elif res == 2:
        print('\033[1;31m Computador vence!')
    else:
        print('\033[1;31m Jogada Invalida!')

if pc == 2:
    if res == 0:
        print('\033[1;31m Computador vence!')
    elif res == 1:
        print('\033[1;34m Jogador vence!')
    elif res == 2:
        print('\033[1;33m Empate!')
    else:
        print('\033[1;31m jogada invalida!')
print('\033[1;36m=-<>-='*3)