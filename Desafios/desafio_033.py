v1 = (int(input('Digite o primeiro valor:')))
v2 = (int(input('Digite o segundo valor')))
v3 = (int(input('Digite O terceiro valor')))
# Verificando quem é o menor
menor = v1
if v2<v1 and v2<v3:
    menor= v2
if v3<v1 and v3<v2:
    menor= v3
print('O menor valor digitado foi {}'.format(menor))
# Verificando quem é o maior
maior = v1
if v2>v1 and v2>v3:
    maior= v2
if v3>v1 and v3>v2:
    maior= v3
print('O maior valor digitado foi {}'.format(maior))