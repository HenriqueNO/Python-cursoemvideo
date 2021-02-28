def leiaint(n):
    """
    -> A função foi criada para ler se o valor digitado é um número inteiro, barrando todos os valores não compativeis
    :param n: valor que será avaliado
    :return: retorno do valor inteiro digitado, se o for.
    Criado por @HN
    """
    while True:
        print(n, end='')
        a = input(str())
        if a.isnumeric():
            n = int(a)
            return n
        else:
            print('\033[1;31mErro! Digite um número inteiro válido\033[m')


# Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
