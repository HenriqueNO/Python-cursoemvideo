s = 0
cont = 0
for c in range(0,6):
    a = int(input('Digite um valor:'))
    if a % 2 == 0:
        s += a
        cont += 1
print('A soma de todos os {} valores par, é {}'.format(cont, s))
