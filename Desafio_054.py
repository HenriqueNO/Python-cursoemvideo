from datetime import date
atual = date.today().year
cont = 0
cont1 = 0
for c in range(1, 8, + 1):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    con = atual - ano
    if con < 18:
        cont += 1
    else:
        cont1 += 1
print(' ')
print('Ao todo teve {} pessoas menores de idade.'.format(cont))
print('Ao todo teve {} pessoas maiores de idade.'.format(cont1))
