print('\033[1;30mCALCULADORA PA:\033[m')
pri = int(input('\033[1mDigite o primeiro termo da PA: '))
razao = int((input('Digite a razão da PA: ')))
termo = pri
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('\033[1;34m', termo, '\033[m', end=' \033[1;31m->\033[m ')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer ver a mais? '))
print('\033[1;33m Pogressão finalizada com {} termos mostrados.'.format(total))



