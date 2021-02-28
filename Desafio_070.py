tet = total = cont = menor = 0
barato = ''
while True:
    nome = str(input('Nome do produto: '))
    pro = float(input('Preço do produto: R$'))
    total += pro
    cont += 1
    if cont == 1 or pro < menor:
        menor = pro
        barato = nome
    if pro > 1000:
        tet += 1
    per = ' '
    while per not in 'SN':
        per = str(input('-> Deseja continuar? ')).upper().strip()[0]
    if per == 'N':
        break
print(' -=-  Analizando dados da compra...  -=-')
from time import sleep
sleep(2)
print('-0-'*20)
print(f' Temos {tet} produto custando mais de R$1000\n O total de sua compra foi R${total:.2f}\n O nome do '
      f'produto mais barato foi \033[1;34m{barato}\033[m, custando R${menor}')
print('-0-'*20)