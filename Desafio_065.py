cont = 0
per = ''
c1 = 0
maior = menor = 0
while per != 'N':
    n = int(input('>>> digite um número: '))
    c1 += n
    cont += 1
    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    per = str(input('Deseja continuar? [Sim/Nao]: ')).upper().strip()[0]
print('A quantidade de número digitados foi {}, e sua média é de {}.'.format(cont, c1 / cont))
print('Maior valor:', maior,'Menor Valor: ', menor)