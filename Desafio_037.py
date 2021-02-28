num = int(input('\033[1;30mDigite um número inteiro: '))
print('\033[1;30mInforme o tipo de Conversão que deseja realizar:\n \033[1;35m> Digite 1, Decimal para Binário.\n > Digite 2, '
             'Decimal para Octal \n > Digite 3, Decimal para Hexadecimal\n\033')
base = int(input('\033[1;31m SUA OPÇÃO-> '))
cores = {'limpo': '\033[m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'verde': '\033[1;32m',
         'ciano': '\033[1;36m'}
from time import sleep
sleep(1)
print('{}{:20}{}'.format(cores['verde'], '=-='*35, cores['limpo']))
if base == 1:
    print('    \033[1;36mRealizando a conversão de Decimal para Binário, o número informado , {} {} {},'
          '\033[1;36m ficará {}{}{}'.format(cores['azul'], num, cores['limpo'], cores['amarelo'], bin(num)[2:], cores['limpo']))

elif base == 2:
    print('    \033[1;36mRealizando a conversao de Decimal para Binário, \033[1;36mo número informado , {}{}{},'
          ' \033[1;36mficará {}{}{}'.format(cores['azul'], num, cores['limpo'], cores['amarelo'], oct(num)[2:], cores['limpo']))

elif base == 3:
    print('    \033[1;36mReazliando a conversão de Decimal para Binário, \033[1;36mo número informado ,{}{}{},'
          ' \033[1;36mficará {}{}{}'.format(cores['azul'], num, cores['limpo'], cores['amarelo'], hex(num)[2:], cores['limpo']))
else:
    print(' {}                     Por favor, informe o número correto da converçao de base!{}'.format(cores['vermelho'],
                                                                                                       cores['limpo']))
print('{}{}{}'.format(cores['verde'], '=-='*35, cores['limpo']))