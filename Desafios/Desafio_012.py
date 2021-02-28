print('Desafio012, a promoção ')
p = float(input('Qual o preço normal do produto?'))
cal = (p / 100) * 10
d = p - cal
print('O preço era {} com um desconto de 10% á vista, ficará {}'.format(p,d))
print('Se a opção de pagamento for parcelada, com 8% de aumento, o preço final ficara em R${}'.format(p +(p /100 * 5)))