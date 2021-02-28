cores = {'limpo': '\033[m',
         'azul': '\033[1;34m',
         'amarelo': '\033[1;33m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'branco': '\033[1;30m'}
print('{}{}{}'.format(cores['verde'], '=-='*20, cores['limpo']))
num1 = float(input('{}Informe um valor: '.format(cores['branco'])))
num2 = float(input('Informe um segundo valor: '.format(cores['limpo'])))
print('{}{}{}'.format(cores['verde'], '=-='*20, cores['limpo']))
if num1 > num2:
    print('- O {}Primeiro valor{} é {}maior{}!'.format(cores['amarelo'], cores['limpo'], cores['azul'], cores['limpo']))
elif num1 < num2:
    print('- O {}Segundo valor{} é {}maior{}!'.format(cores['amarelo'], cores['limpo'], cores['azul'], cores['limpo']))
else:
    print('- {}Não existe{} valor maior, os dois são {}iguais!{}!'.format(cores['amarelo'], cores['limpo'],
                                                                          cores['azul'], cores['limpo']))
print('{}{}{}'.format(cores['verde'], '=-=' * 20, cores['limpo']))