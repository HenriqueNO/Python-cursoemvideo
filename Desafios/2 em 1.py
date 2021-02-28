from re import sub
perg = input('Qual operação dejesa realizar? hipotenusa ou ângulo?').strip().lower()
new = sub('[^â\\\]','',perg)
#from math import radians, cos, tan, hypot
print(new)
#if new == 'hipotenusa':
    #op = int(input('Informe o valor do cateto oposto: '))
    #ad = int(input('Informe o valor do cateto adjacente: '))
    #hi = hypot(op, ad)
    #print('O valor da Hipotenusa é de {:.2f}'.format(hi))
#if new == 'angulo':
    #se = int(input('Informe o ângulo: '))
    #seno = radians(se)
    #print('O Seno do ângulo {}, é {}'.format(se, seno))
    #coss = cos(radians(se))
    #print('O Cosseno do ângulo {}, é {}'.format(se, coss))
    #ta = tan(radians(se))
    #print('A Tangente do ãngulo {}, é {}'.format(se, ta))