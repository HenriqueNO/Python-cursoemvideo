import ansi
r1 = float(input('Digite o valor de uma das retas:'))
r2 = float(input('Digite o valor de outra reta:'))
r3 = float(input('Digite o valor da ultima reta:'))
p1 = r1 + r2
p2 = r1 + r3
p3 = r3 + r2
print('=-='*8, ' RESPOSTA ', '=-='*8)
if p1 > r3 and p2 > r2 and p3 > r1:
    print('    É possivel formar um triângulo com essas 3 retas!')
else:
    print('    Impossivel formar um triângulo com essas 3 retas!')
print('=-='*20)
