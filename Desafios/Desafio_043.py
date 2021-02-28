peso = float(input('Informe o seu peso: '))
altura = float(input('infome sua altura: '))
calc = peso / (altura * altura)
from time import sleep
sleep(0.5)
if calc <= 18.5:
    print('\033[1;31mAbaixo do peso\033[m, IMC= {:.2f}'.format(calc))
elif calc <= 25:
    print('\033[1;33mPeso ideal\033[m, IMC= {:.2f}'.format(calc))
elif calc <= 30:
    print('\033[1;32mSobrepeso\033[m, IMC= {:.2f}'.format(calc))
elif calc >= 31:
    print('\033[1;33mObesidade\033[m, IMC= {:.2f}'.format(calc))
elif calc > 40:
    print('\033[1;31mObesidade mórbida\033[m, IMC= {:.2f}'.format(calc))