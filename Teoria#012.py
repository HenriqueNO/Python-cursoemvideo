nome = str(input('Qual é seu nome? ')).strip().lower()
if nome == 'henrique':
    (print('Que nome bonito! '))
elif nome in 'ana claudia jessica juliana':
    print('Belo nome moça!')
else:
    print('Prazer em te conhecer')
print('Tenha um bom dia, {}!'.format(nome))