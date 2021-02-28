sala = float(input('Qual o salário do funcionario?'))
if sala >= 1251:
    sa = sala * 10 / 100
    t= sa + sala
    print(' O salário do funcionario era de R${:.2f}, e com o aumento de 10%(R${:.2f}), foi para R${:.2f}'.format(sala, sa, t))
if sala <= 1250:
    s15 = sala * 15 / 100
    to = s15 + sala
    print(' O salário do funcionario era de R${:.2f}, e com o aumetno de 15%(R${:.2f}), foi para R${:.2f}'.format(sala, s15, to))