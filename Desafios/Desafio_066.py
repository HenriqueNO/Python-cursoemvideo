cont = res = 0
n = int(input('Quer ver a tabuada de qual valor? '))
while True:
    cont += 1
    res = n * cont
    print(f'{n} X {cont} = {res}')
    if cont >= 10:
        n = int(input('Digite outro número para ver sua tabuada: '))
        cont = res = 0
    if n <= -1:
        break
print('Finish!')



