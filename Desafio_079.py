
lista = []
p = ''
while p != 'n':
        n = int(input('Digite um número: '))
        if n not in lista:
                lista.append(n)
        else:
                print('Valor duplicado, número não adicionado')
        p = str(input('Deseja continuar? [S/N] ')).lower().strip()[0]
        while True:
                if p != 's' and p != 'n':
                        p = input('Deseja continuar? [S/N] ').lower().strip()[0]
                else:
                        break
lista.sort()
print(f'{"-=-"*13}')
print(f'Você digitou os números: {lista}')
