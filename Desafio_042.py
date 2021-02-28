cores = {'limpo': '\033[m',
         'branco': '\033[0;30m',
         'vermelho': '\033[0;31m',
         'verde': '\033[0;32m',
         'amarelo': '\033[0;33m',
         'azul': '\033[0;34m',
         'roxo': '\033[0;35m',
         'azulm': '\033[0;36m',
         'cinza': '\033[0;37m'}
coresneg = {'brancon': '\033[1;30m',
         'vermelhon': '\033[1;31m',
         'verden': '\033[1;32m',
         'amarelon': '\033[1;33m',
         'azuln': '\033[1;34m',
         'roxon': '\033[1;35m',
         'azulmn': '\033[1;36m',
         'cinzan': '\033[1;37m'}


r1 = float(input('{}Informe o valor da primeira reta do triângulo: '.format(cores['branco'])))
r2 = float(input('Informe o valor da segunda reta do triângulo: '))
r3 = float(input('Informe o valor da teceira reta do triângulo:{} '.format(cores['limpo'])))
p1 = r1 + r3
p2 = r1 + r2
p3 = r2 + r3
if p1 > r3 and p2 > r2 and p3 > r1:
    print('{}É possivel formar um triângulo como essas três retas!{}'.format(coresneg['amarelon'], cores['limpo']))
if r1 == r2 != r3:
    print('É um {}triângulo isósceles{}: dois lados iguais!'.format(coresneg['azuln'], cores['limpo']))
elif r1 != r2 != r3:
    print('É um {}triângulo escaleno{}: todos os lados diferentes!'.format(coresneg['azuln'], cores['limpo']))
elif r1 == r2 == r3:
    print('É um {}triângulo Equilátero{}: todos os lados iguais!'.format(coresneg['azuln'], cores['limpo']))
else:
    print('{}Impossivel formar um triângulo com essas três retas{}!'.format(coresneg['vermelhon'], cores['limpo']))