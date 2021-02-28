print('=-='*4, 'Desafio017', '=-='*4)
import math
ad = float(input('Quanto mede o cateto adjacente do triangulo?'))
op = float(input('Quanto mede o cateto oposto do triangulo?'))
h = math.hypot(op,ad)
print('A hipotenusa medira {:.2f}'.format(h))
seno = op / h
cosse = ad / h
print('Seno será {:.2f}\n Cosseno será {:.2f}'.format(seno, cosse))
