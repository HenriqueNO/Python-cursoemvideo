from utilidades import moeda

p = float(input('Digite o preço: R$'))
print(f'Metade de {moeda.moeda(p)} é {moeda.moeda(ex107.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(ex107.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos R${moeda.moeda(moeda.diminuir(p, 13))}')