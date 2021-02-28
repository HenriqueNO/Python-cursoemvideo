#Listas:

#.append(), para adicionar um elemento novo na lista.
#.insert(), para adicionar um elemento em outra posição.
# Del exemplo[indece] para eliminar um elemento da lista.
# exemplo.pop[indece] para eliminar um elemento da lista.
# exemplo.remove['valor'] para eliminar um elemento da lista.

#num = [2, 1, 3, 5, 4]
#print(num)

#num[1] = 10
#num.append(6)
#print(num)

#num.sort()
#print(num)

#num.insert(2, 0)
#print(num)

#num.pop(2)
#print(num)

valores = list() #[]
valores.append(3)
valores.append(4)
valores.append(5)

for c, v in enumerate(valores):
    print(f"Na posição {c}, encontrei o número {v}!")
print('Finalizei a lista')