print('-------------------------------')
print('\033[1;30m Master Calculadora.')
print('\033[1m Digite dois valores!')
print('-------------------------------')
v1 = float(input(' Valor 1: '))
v2 = float(input(' Valor 2: '))
print('-------------------------------')
'''print('\033[1;34m MENU DE OPÇÕES:\033[m')
print('-------------------------------')
print(' [1] Somar.\n [2] Multiplicar\n [3] Maior\n [4] Nos números\n [5] Sair do programa')
print('-------------------------------')'''
esco = 1
maior = 0
while esco != 5:
    print(' [1] Somar.\n [2] Multiplicar\n [3] Maior\n [4] Novos números\n [5] Sair do programa')
    print('-------------------------------')
    esco = int(input('>>>>>>> Qual sua opção? '))
    if esco == 1:
        c1 = v1 + v2
        print('\033[1;33mO resultado de {} + {} = {}\033[m'.format(v1, v2, c1))
        print('-------------------------------')
    elif esco == 2:
        c1 = v1 * v2
        print('\033[1;33mO resultado de {} x {} = {}\033[m'.format(v1, v2, c1))
    elif esco == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('\033[1;33mEntre {} e {} o maior é {}\033[m'.format(v1, v2, maior))
    elif esco == 4:
        v1 = float(input('Digite o novo valor: '))
        v2 = float(input('Digite outro novo valor: '))
    else:
        print('\033[1;31mOpção inválida, tente novamente\033[m')
from time import sleep
print('Finalizando...')
sleep(2)
print('\033[1;36mFim do pograma!')
