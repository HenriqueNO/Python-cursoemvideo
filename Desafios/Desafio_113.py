def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mErro! Digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usario não informou os valores.')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            nr = float(input(msg))
        except (KeyboardInterrupt):
            print('O usario não informou os valores.')
            return 0
        except:
            print('\033[1;31mErro! Digite um número real valido\033[m')
        else:
            return nr


# Programa principal
n = leiaint('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')
nr = leiafloat('Digite um número real: ')
print(f'Você acabou de digitar o número {nr}')