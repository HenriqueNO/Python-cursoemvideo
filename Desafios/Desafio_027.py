nome = str(input('Informe seu nome completo:')).strip()
sep = str.split(nome)
print('Seu primeiro nome é {}.'.format(sep[0]))
print('Seu último nome é {}.'.format(sep[len(sep)-1]))