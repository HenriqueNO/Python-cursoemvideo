from utilidades import moeda

p = float(input('Digite o preço: R$'))
print(f'Metade de {moeda.moeda(p)} é {moeda.metade(p, show=True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, show=True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, show=True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, show=True)}')