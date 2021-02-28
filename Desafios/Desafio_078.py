List = []
for c in range(0, 5):
    List.append(int(input(f'Digite um número para a {c}º: ')))
print(f'Você digitou os valores: {List}')
mai = max(List)
print(f'O maior valor digitado foi {max(List)}, encontrado na posição ', end='')
for i, v in enumerate(List):
    if List[i] == mai:
        print(f'{i}', end='... ')
men = min(List)
print(f'\nO menor valor digitado foi {min(List)} encontrado na posição ', end='')
for i, v in enumerate(List):
    if List[i] == men:
        print(f'{i}', end='... ')