lista1 = []
lista2 = []
lista3 = []
p = ''
from time import sleep

while p != 'n':
    n = int(input('Digite um número: '))
    lista1.append(n)
    if n % 2 == 0:
        lista2.append(n)
        print('Número PAR, adicionado na lista 2.')
    else:
        lista3.append(n)
        print('Número IMPAR, adicionado na lista 3.')
    p = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    while p != 'n' and p != 's':
        p = str(input('Resposta invalida, deseja continuar? [S/N] ')).lower().strip()[0]

print('\033[1;30;4mCOMPUTANDO...\033[m')
sleep(1)

print(f'Lista piloto: {lista1}\nLista com números pares: {lista2}\nLista com os números impares: {lista3}')