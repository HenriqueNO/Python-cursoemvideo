f = str(input('Digite um frase:')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(f.count('A')))
print('A primeira letra A apareceu na posição {} da frase'.format(f.find('A')+1))
print('A ultima letra A aparece na posição {} da frase'.format(f.rfind('A')+1))