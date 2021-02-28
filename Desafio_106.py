def helpme():
    """
    -> Uma função com help mais personalizado com cores
    :return: retorna com o comando que você deseja ver o manual
    """
    perg = ''
    while perg != 'fim':
        print('\033[1;31m~~'*20)
        print(f'{"SISTEMA DE AJUDA PYHELP":^40}')
        print('~~'*20, '\033[m')
        perg = str(input('Função ou Biblioteca > ')).lower().strip()
        if perg != 'fim':
            print('\033[1;32m~~' * 20)
            print(f'  Acessando o manual do comando {perg}')
            print('~~' * 20, '\033[m')
            print('\033[1;34m')
            help(perg)
            print('\033[m')
    print('\033[1;32m~~'*6)
    print('  Até logo!')
    print('~~'*6, '\033[m')
helpme()