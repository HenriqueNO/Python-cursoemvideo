est = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze',
'desesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um numero, entre 0 e 20: '))

while True:
    if num < 0 or num > 20:
        num = int(input('Tente novamente, Digite um número entre 0 e 20: '))
    else:
        break
a = est[num]
print(f'Você digitou o número \033[32m{str.upper(a)}\033[m')