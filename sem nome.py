media = 0
mcont = 0
homemvelho = 0
nomedoveio = ''
mulher = 0
for c in range(1, 5, +1):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: '))
    media += idade
    if c == 1 and sexo in 'Mm':
        homemvelho = idade
        nomedoveio = nome
    if sexo in 'Mm' and idade > homemvelho:
        homemvelho = idade
        nomedoveio = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1


mcont = media / 4
print('Media de idade do grupo é de {}'.format(mcont))
print('O homem mais velho se chama {} e ele tem {} anos'.format(nomedoveio, homemvelho))
print('Ha {} mulheres com menos de 20 anos'.format(mulher))