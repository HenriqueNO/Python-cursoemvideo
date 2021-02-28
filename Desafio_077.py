p = ('Empreendedor', 'Sucesso', 'Milionario')
for v in p:
    print(f'\nNa palavra {v.upper()} temos: ', end='')
    for l in v:
        if l.lower() in 'aeiou':
            print(l, end=' ')