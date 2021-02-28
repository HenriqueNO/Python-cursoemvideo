def fatorial(n, show=False):
    """
    -> Essa função faz o fatorial de um número e mostra ou não seu processo na tela
    :param n: Número no qual você deseja fazer o fatorial
    :param show: Show=True ou Show=False se você deseja ou não que a função mostre o processo.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)