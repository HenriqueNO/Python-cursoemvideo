from time import sleep
from random import randint
from operator import itemgetter
game = {'player1': randint(1, 6),
        'player2': randint(1, 6),
        'player3': randint(1, 6),
        'player4': randint(1, 6)
        }

ranking = list()
print('Valores sorteados:')
sleep(1)
for k, v in game.items():
    print(f'O {k.upper()} tirou o número {v} no dado')
    sleep(0.8)
print()
print('Ranking dos jogadores:')
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)        #vira lista

for i, v in enumerate(ranking):
    print(f'{i + 1}º Lugar: {v[0].upper()} com número {v[1]} do dado')
    sleep(0.8)