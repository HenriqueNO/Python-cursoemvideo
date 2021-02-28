nome = str(input('Qual é o seu nome?')).strip()
cores = {'limpa':'\033[m',
         'azul':'\033[1;34m',
         'amarelo sub':'\033[4;34m',
         'verde':'\033[1;32m',
         'amarelo neg':'\033[1;33m'}
print('Olá! Muito prazer em te conhcer, {}{}{}'.format(cores['azul'], nome, cores['limpa']))