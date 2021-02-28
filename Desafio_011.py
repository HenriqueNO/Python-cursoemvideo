print('Desafio011, Pintando uma parede')
L = float(input('Quanto de largura tem sua parede?'))
H = float(input('Quanto de altura tem sua parede?'))
R = L * H
T = R / 2
print('A área de sua parede é de {}m², sabendo que 1L de tinta pinta 2m² sera necessario {:.3}L de tinta para pintar essa parede'.format(R,T))