def area (a, b):
    A = a * b

    print(f'A área de um terreno é de {a:.2f} X {b:.2f} é de {A:.2f}m²')


def tit():
    print()
    print(f'{"Controle de terrenos":>20}')
    print('---' * 10)


tit()
a = float(input('Largura (m): '))
b = float(input('Complimento (m): '))
area(a, b)