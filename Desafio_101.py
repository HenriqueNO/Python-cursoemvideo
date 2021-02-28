from datetime import datetime
ano = datetime.now()


def voto():
    global vot
    vot = ano.year - nasc
    return vot

print('--'*20)
nasc = int(input('Informe o ano em que nasceu: '))
vota = voto()
print(f'Com {vot} anos: ', end='')
if vota < 16:
    print('VOTO NEGADO')
elif vota >= 18:
    if vota > 65:
        print('VOTO OPCIONAL')
    else:
        print('VOTO OBRIGATORIO')

else:
    print('VOTO OPCIONAL')