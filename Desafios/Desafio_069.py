M = F = P = 0
cont = 0
while True:
    print('\033[1;30m=-='*10)
    print('  Cadastre uma pessoa:')
    print('=-=' * 10, '\033[m')
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if sexo == 'M':
            M += 1
            break
        elif sexo == 'F':
            if idade < 20:
                F += 1
            break
    if idade > 18:
        P += 1
    print('\033[1;30m=-=' * 10)
    while True:
            perg = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
            if perg == 'N':
                break
            elif perg == 'S':
                break
    if perg == 'N':
        break
from time import sleep
print('Analizando dados...')
sleep(1)
print(f'Foi constatado que, {P} pessoa(s) tem mais de 18 anos, {M} homen(s) foram registrados, {F} mulher(es) tem menos de 20 anos')
print('Todos os dados foram registrados!')
