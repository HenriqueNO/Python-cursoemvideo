salario = float(input('Informe seu salário: R$'))
valorcasa = float(input('Informe o valor da casa: R$'))
anos = int(input('Informe por quantos anos você vai pagar a casa: '))
prestaçao = valorcasa / (anos * 12)
minimo = salario * 30 / 100
if minimo >= prestaçao:
    print('Emprestimo aprovado!\n Para pagar a casa do valor R${} em {} anos\n'
          ' A prestaçao será de R${:.2f}'.format(valorcasa, anos, prestaçao))
else:
    print('Emprestimo negado!')