n = int(input('Digite um valor: '))
cont = 0
c1 = 0
while n != 999:
    cont += 1
    c1 += n
    n = int(input('Digite outro valor (para parar digite 999): '))
print('Numeros digitados: ', cont)
print('Somatorio dos valores: ', c1)
