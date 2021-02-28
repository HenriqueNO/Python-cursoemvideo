a = str(input('Digite a expressão: '))
p = []
for simb in a:
    if simb == '(':
        p.append('(')
    elif simb == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('A expessão é valida!')
else:
    print('A expressão é invalida')