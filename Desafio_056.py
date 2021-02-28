sidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher = 0
for c in range(1, 5):
    print('{} \033[1;31m{}ª PESSOA\033[m {}'.format('-'*4, c, '-'*4,))
    nome = str(input('Nome? ')).strip()
    idade = int(input('Idade? '))
    sexo = str(input('Qual seu sexo? [M/F]:  ')).strip()
    sidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1

mediaidade = sidade / 4
print('A média da idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('São {} mulheres que tem menos de 20 anos.'.format(mulher))