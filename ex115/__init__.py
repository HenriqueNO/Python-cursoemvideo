dados = {}


def linha(tam=25):
    a = '\033[1;30m'
    print(f'{a}{"--" * tam} \033[m')


def mensagem(msg):
    linha()
    print(f'  {msg:^45}')
    linha()

def menu(lista):
    mensagem('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    linha()
    while True:
        opc = leiaint('Sua opção: ')
        if opc >= c:
            linha()
            print('\033[1;31m  Opção inválida, tente digitar o codigo certo.\033[m')
            linha()
        else:
            break
    return opc


def leiaint(n):
    while True:
        a = input(n)
        if a.isnumeric():
            n = int(a)
            return n
        else:
            print('\033[1;31mErro! Digite uma opção válida\033[m')