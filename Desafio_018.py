print('=-='*4, 'Desafio018', '=-=*'*4)
from math import radians, cos, tan
ang = float(input('Digite um angulo:'))
seno = radians( ang )
print('O ângulo de {}, tem o SENO de {:.3f}'.format(ang, seno))
cosse = cos(radians(ang))
print('O ângulo de {}, tem o COSSENO de {:.3f}'.format(ang,cosse))
tang = tan(radians(ang))
print('O ângulo de {}, tem a TAGENTE de {:.3f}'.format(ang,tang))