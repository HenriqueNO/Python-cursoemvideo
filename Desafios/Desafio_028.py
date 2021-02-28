perg = int(input('Vou pensar em um numero de 0 a 5, tente advinhar!\n Em qual número eu pensei?'))
from random import randint
from time import sleep
print('PROCESSANDO...')
sleep(2)
num = randint(0, 5)
if num == perg:
    print('=-='*8, ' PARABÉNS!!! ','=-='*8)
    print('        O número escolhido era {}!'.format(num))
else:
    print( '=-='*8, ' Computador venceu ', '=-='*8,'\n                    O número que eu pensei foi {}'.format(num))
if perg >= 6:
    print('!!! Você digitou um número maior que 5, vamos tentar denovo? !!!')
print('=-='*23)