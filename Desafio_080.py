lista = []
for a in range(0, 5):
    n = int(input('Digite um número: '))
    if a == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado na ultima posição da lista!')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos + 1} da lista!')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')