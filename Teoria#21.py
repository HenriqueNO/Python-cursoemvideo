# Funções

# help()  # ajuda interativa
# print(input.__doc__) #mostra informações sobre um comando


def contador(i, f, p):  # criando um help interativo de contador
    """
    -> Faz uma contagem e mostra na tela
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: sem retorno
    """

    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


def somar(a=0, b=0, c=0):  # Parametros opcionais
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    Função criada por @HN
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(1, 4, 5)
somar(2, 4)
