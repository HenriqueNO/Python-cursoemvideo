nome = str(input('Qual é seu nome completo?')).strip()
print('Seu nome em letras minúsculas, fica {}'.format(nome.lower()))
print('Seu nome em letras maiúsculas, fica {}'.format(nome.upper()))
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

st = str.split(nome)
print('Seu primeiro nome é {}, e ele tem {} letras'.format(st[0], len(st[0])))