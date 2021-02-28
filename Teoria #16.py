#Tuplas

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}')

for c in lanche:
    print(f'Eu vou comer {c}')

#Tuplas: São imutáveis

                            #Organizando:

#print(sorted(lanche))
#print(lanche)


#a = (2, 5, 4)
#b = (5, 8, 1, 2)
#c = b + a
#print(sorted(c))
#print(c.index(4, 2))

                            #Deletando uma Tupla.

#pessoa = ('henrique', 16, 'M', 60.50)
#del(pessoa)
#print(pessoa)