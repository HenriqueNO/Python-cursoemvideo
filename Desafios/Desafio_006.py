print('desafio006')
n1 = int(input('Digite um número:'))
db = n1 * 2
tp = n1 * 3
rz = n1 ** (1/2)
#print('Número digitado: {}\n Doblo do número: {}\n Triplo do número: {}\n Raiz quadrada: {:.2f}'.format(n1,db,tp,rz))
print('O valor digitado: {}\n Doblo do valor digitado: {} \n Triplo do valor digitado: {}\n Raiz quadrada do valor digitado: {:.2f}'.format(n1,n1 * 2,n1 * 3,pow(n1,(1/2))))