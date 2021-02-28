dados = []
infos = {}
mulheres = []

p = ''
soma = media = 0
while p != 'n':
    infos.clear()
    infos['nome'] = str(input('Nome: '))
    infos['idade'] = int(input('Idade: '))
    soma += infos['idade']
    while True:
        infos['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if infos['sexo'] in 'MF':
            break
        else:
            print('\033[1;33mERRO!\033[m Por favor digite apenas M ou F.')
    dados.append(infos.copy())

    while True:
        p = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
        if p in 'sn':
            break
        else:
            print('\033[1;33mERRO!\033[m Digite apenas S ou N.')

print('-=-' * 15)
print(dados)
print('-=-' * 15)

if len(dados) > 1:
    print(f'- Ao todo temos {len(dados)} pessoas cadatradas')
else:
    print(f'- Ao todo temos {len(dados)} pessoa cadatrada')

media = soma / len(dados)
print(f'- A média da idade das pessoas cadastradas é de {media:5.2f} anos')

print(f'- A mulheres cadastradas foram: ', end='')
for p in dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=', ')
print()
print('- Lista das pessoas acima da média: ')
for p in dados:
    if p['idade'] >= media:
        print('  ', end='')
        for k, v in p.items():
            print(f' {k.upper()} = {v}', end='')
print()
print('<< Dados apresentados >>')