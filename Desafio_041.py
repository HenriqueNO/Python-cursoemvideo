cores = {'limpo': '\033[m',
         'azul': '\033[1;34m',
         'branco': '\033[1;30m',
         'verde': '\033[1;32m'}
from datetime import date
atual = date.today().year
ano = int(input('{}Informe o ano de nascimento:{} '.format(cores['branco'], cores['limpo'])))
idade = atual - ano
print('{}{}{}'.format(cores['branco'], '-=-'*20, cores['limpo']))
print('Considerando sua idade de {}{} Anos{}:'.format(cores['verde'], idade, cores['limpo']))
if idade <= 9:
    print('Sua categoria é {}Mirin{} (menor de 9 anos).'.format(cores['azul'], cores['limpo']))
elif idade <= 14:
    print('Sua categoria é {}Infantil{} (10 ate 14 anos).'.format(cores['azul'], cores['limpo']))
elif idade <= 19:
    print('Sua categoria é {}Junior{} (15 ate 19).'.format(cores['azul'], cores['limpo']))
elif idade <= 25:
    print('Sua categoria é {}Sênior{} (20 até 25 anos).'.format(cores['azul'], cores['limpo']))
else:
    print('Sua categoria é {}Master{} (acima de 25 anos).'.format(cores['azul'], cores['limpo']))
print('{}{}{}'.format(cores['branco'], '-=-' * 20, cores['limpo']))