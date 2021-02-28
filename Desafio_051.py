prim = int(input('Informe o primeiro termo da pogressão aritmética: '))
razao = int(input('Informe razão da pogressão aritmética: '))
termo = 10 * razao
for c in range(prim, termo, razao):
    print('{}{}{}'.format('\033[1;34m', c, '\033[m'), end='\033[1;31m->\033[m')
print('\033[1;33mFim.')