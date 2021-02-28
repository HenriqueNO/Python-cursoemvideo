print('\033[1;30mCALCULADORA PA:\033[m')
pri = int(input('\033[1mDigite o primeiro termo da PA: '))
razao = int((input('Digite a razão da PA: ')))
termo = pri
cont = 1
from time import sleep
print('CALCULANDO...')
sleep(2)
while cont <= 10:
    print('\033[1;34m', termo, '\033[m', end=' \033[1;31m->\033[m ')
    termo += razao
    cont += 1
print('\033[1;33m FIM')