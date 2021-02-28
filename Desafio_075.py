num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o ultimo número: ')))
print(f'Você digitou os números {num}')
print(f'O valor nove aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O valor três aparece na {num.index(3)+1}ª posição')
else:
    print('O valor três não apareceu em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')