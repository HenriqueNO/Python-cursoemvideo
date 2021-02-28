from time import sleep
def contador(a, b, c):
    cont = 0
    print('=-='*12)
    print(f' Contagem de {a} até {b} de {c} em {c}.')
    print(f' {a}', end=' ')
    if a < b:
        while a <= b:
            a += c
            sleep(0.3)
            if a > b:
                a = a - c
                break
            print(f'{a}', end=' ')
        print('FIM!')

    elif a > b:
        while a >= b:
            a -= c
            sleep(0.3)
            if a < b:
                a = a + c
                break
            print(f'{a}', end=' ')
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez, escolha os números da contagem!')
a = int(input('Início: '))
b = int(input('Fim:    '))
c = int(input('Passo:  '))
if c < 0:
    c = c - c - c
elif c == 0:
    c = c + 1
contador(a, b, c)