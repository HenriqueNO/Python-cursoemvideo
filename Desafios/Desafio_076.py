print('-'*51)
print(f' {"=-="*5} \033[1;34mListagem de preço\033[m {"=-="*5}')
print('-'*51)
itens = ('Lápis', 'Borracha', 'Caderno', 'Estojo',
         'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livro')
preço = 1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90
for c in range(0, len(itens)):
    print(f' {itens[c]:.<40} R$ {preço[c]:>6.2f}')
print('-' * 51)