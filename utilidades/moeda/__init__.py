def metade(n, show=False):
    n = n / 2
    if show:
        return f'R${int(n)},00'
    return n


def dobro(n, show=False):
    n = n * 2
    if show:
        return f'R${int(n)},00'
    return n


def aumentar(n, p, show=False):
    r = (n * p) / 100
    r = n + r
    if show:
        return f'R${int(r)},00'
    return r


def diminuir(n, p, show=False):
    r = (n * p) / 100
    r = n - r
    if show:
        return f'R${int(r)},00'
    return r


def moeda(n):
    n = f'R${int(n)},00'
    return n


def resumo(n, pma=0, pme=0):
        print('---' * 10)
        print(f'{"Resumo do valor":^30}')
        print('---' * 10)
        pra = f'R${int(n)},00'
        print(f'Preço analisado:  {pra:>12}')
        mul = n * 2
        d = f'R${int(mul)},00'
        print(f'Dobro do preço:   {d:>12}')
        me = n / 2
        m = f'R${str(me).replace(".", ",")}'
        print(f'Metade do preço:  {m:>12}')
        por = (n * pma) / 100
        pa = n + por
        a = f'R${str(pa).replace(".", ",")}'
        print(f'{pma}% de aumento:   {a:>12}')
        por1 = (n * pme) / 100
        re = n - por1
        r = f'R${str(re).replace(".", ",")}'
        print(f'{pme}% de redução:   {r:>12}')
        print('---' * 10)