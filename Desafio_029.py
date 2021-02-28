mult = float('7')
Velo = float(input('Qual a velocidade registrada do veiculo?'))
print('=-='*20)
if Velo >= 81:
    mu = (Velo - 80) * 7.00
    print('  Você foi multado, excesso de velocidade!\n  passou a {}Km/h, numa pista de 80Km/h'.format(Velo))
    print('  O preço a pagar será de R${}'.format(mu))
else:
    print('               Tenha um bom dia! \n               Dirija com cuidado!')
print('=-='*20)