from random import randint
alea = randint(0, 10)
print('---------------------------------------------------------------------')
print('Sou seu computador... Acabei de pensar em um número, tente advinha =D')
print('---------------------------------------------------------------------')
num = 0
num1 = 0
num += 1
s = int(input('\033[1;32mFaça o primeiro chute:\033[m '))
while s != alea:
    if s < alea:
        print('\033[1;36mMais...')
    if s > alea:
        print('\033[1;36mMenos...')
    if s != alea:
        s = int(input('\033[1;31mDigite outro número:\033[m '))
    num1 += 1
print('----------------------------------------------------------------------------')
print('\033[1;34mVocê acertou\033[m, eu pensei no número {}, foram {} tentativa(s).'.format(alea, (num + num1)))
print('----------------------------------------------------------------------------')