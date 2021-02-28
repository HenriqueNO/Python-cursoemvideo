per = int(input('Qual a distância da sua viagem?'))
if per <= 200:
    vp = per * 0.50
    print('A distância: {}\n O valor de sua viagem será de R${}'.format(per, vp))
else:
    vg = per * 0.45
    print('A distância: {}\n O valor de sua viagem será de R${}'.format(per, vg))
