info = {'nome': '', 'media': ''}
info['nome'] = input('Nome: ')
info['media'] = float(input(f'Média de {info["nome"]}: '))
print()

print(f'Nome é igual a {info["nome"]}')
print(f'Média é igual a {info["media"]}')
if info['media'] >= 7:
    print('Situação do aluno igual a Aprovado!')
elif info['media'] < 7:
    print('Situação do aluno igual a Recuperação!')
else:
    print('Situação do alino igual a Reprovado!')