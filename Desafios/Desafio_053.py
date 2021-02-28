frase = str(input('Escreva um frase: ')).strip().lower()
palavras = frase.split()
join = ''.join(palavras)
#inverso = ''
inverso = join[::-1]  #Fatiamento!
#'''for c in range(len(join) - 1, -1, -1):      #Usando o metodo for
    #inverso += join[c]
print('O inverso de {} é {}'.format(join, inverso))

if inverso == join:
    print('Temos um palídromo!')
else:
    print('A frase nao é um palídromo!')