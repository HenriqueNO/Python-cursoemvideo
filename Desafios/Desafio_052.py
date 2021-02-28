tot = 0
inte = int(input('Digite um valor: '))
for c in range(1, inte + 1):
    if inte % c == 0:
        print('\033[1;33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\nO número {} foi divisível {} vezes'.format(inte, tot))
if tot == 2:
    print('E por isso ele é \033[1;34mPRIMO\033[m.')
else:
    print('E por isso ele \033[1;34nao é PRIMO\033[m.')