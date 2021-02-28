n1 = float(input('Informe a primeira nota do aluno: '))
n2 = float(input('Informe a segunda nota do aluino: '))
conta = (n1 + n2) / 2
if conta < 5.0:
    print('\033[1;31mREPROVADO\033[m! Você teve a media de\033[1;31m {:.1f}\033[m, \n\033[1;31mestude mais\033[m!'.format(conta))
elif conta < 6.9:
    print('Estude para a recuperação, você teve a media de\033[1;33m {:.1f}\033[m'.format(conta))
elif conta < 10.1:
    print('Parabéns, você tem media de \033[1;34m{:.1f}'.format(conta))
else:
    print('\033[1;31mERRO\033[m\n\033[1;30mPor favor, digite o valor da nota do aluno corretamente.')