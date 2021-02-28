print('---------------------------------------')
print(' Digite um número e veja seu fatorial!')
print('---------------------------------------')
num = int(input(' Digite um número: '))
c = num
f = 1
from time import sleep
print('Calculando '
      'o fatorial de \033[1;33m{}!\033[m ='.format(num), end='')
while c > 0:
    print(' \033[1;36m{}\033[m'.format(c), end='')
    print(' \033[1;30mx\033[m' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('\033[1;34m{}'.format(f))

