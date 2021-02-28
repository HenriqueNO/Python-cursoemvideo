lista = []
p = ''
while p != 'n':
    n = lista.append(int(input('Digite um valor: ')))
    p = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
    while True:
        if p != 's' and p != 'n':
            p = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
        else:
            break
print(f'Você teclou {len(lista)} números.')
lis = lista[:]
lis.sort(reverse=True)
print(f'O números em ordem decrescente: {lis}')
lis.sort(reverse=False)
if 5 in lista:
    print(f'O valor 5 faz parte da lista!\n{lista.index(5)+1}ª posição CRESCENTE\n{lis.index(5)+1}ª posição DECRESCENTE')
else:
    print('O valor CINCO não faz parte da lista')