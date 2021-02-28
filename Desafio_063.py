termo = int(input('Digite quanto termos deseja ver da sequencia de Fibinacci: '))
f = 0
c = 0
a = 1
while termo >= c:
    c += 1
    f += a
    print(a, end=', ')
    a += f
    print(f, end=', ')
print('Fim')

