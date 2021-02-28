cores = {'limpo': '\033[m',
         'brancon': '\033[1;30m',
         'vermelhon': '\033[1;31m',
         'verden': '\033[1;32m',
         'amarelon': '\033[1;33m',
         'azuln': '\033[1;34m',
         'roxon': '\033[1;35m',
         'azulmn': '\033[1;36m',
         'cinzan': '\033[1;37m'}
print('{}{}{}'.format(cores['azulmn'], '-=-'*20, cores['limpo']))
opçao = str(input('\033[0;33mEscolha a opção de pagamento:\033[m \n (1) À \033[1;34mvista dinheiro/cheque\033[m: 10% desconto.\n'
                  ' (2) À \033[1;34mvista no cartão\033[m: 5% de desconto\n (3) Em até \033[1;34m2x no cartao\033[m: preço normal\n'
                  ' (4) Em até \033[1;34m3x ou mais no cartão\033[m: 20% de juros\n Opção de pagamento: ')).strip()
print('{}{}{}'.format(cores['azulmn'], '-=-'*20, cores['limpo']))
if opçao == '1':
    preço = float(input('Infome o preço do produto: '))
    a1 = preço - (preço * 10 / 100)
    print('À vista no dinheiro/cheque, o preço do produto ficará R${}'.format(a1))
elif opçao == '2':
    preço = float(input('Infome o preço do produto: '))
    print('{}{}{}'.format(cores['azulmn'], '-=-' * 20, cores['limpo']))
    a2 = preço - (preço * 5 / 100)
    print('À vista no cartão, o preço do produto ficará R${}'.format(a2))
elif opçao == '3':
    preço = float(input('Infome o preço do produto: '))
    print('{}{}{}'.format(cores['azulmn'], '-=-' * 20, cores['limpo']))
    a3 = preço / 2
    print('Em ate x2 no cartao, o preço do produto será normal, mas com duas parcelas de R${}'.format(a3))
elif opçao == '4':
    preço = float(input('Infome o preço do produto: '))
    quant = int(input('Em quantas vezes deseja pagar? '))
    a3 = preço + (preço * 20 / 100)
    t = a3 / quant
    print('Em {}x no cartão tera 20% de juros com parcelas de R${}, e o preço total será de R${}'.format(quant, t, a3))
else:
    print('Opção de pagamento nao valida, tente outra vez!')
print('{}{}{}'.format(cores['azulmn'], '-=-'*20, cores['limpo']))