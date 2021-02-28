print('Desafio008')
M = int(input('Digite um valor em metros:'))
Cm = M * 100
km = M / 1000
mm = M * 1000
dm: int = M * 10
hm = M / 100
dam = M / 10
print('Quilômetro {}\n Hectômetro: {} \n Decâmetro: {}\n Metro: {}\n Decímetro: {}\n Centímetro: {}\n Milímetro: {}'.format(km,hm,dam,M,dm,Cm,mm))