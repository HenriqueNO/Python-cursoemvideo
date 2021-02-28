desem = {}
dados = []

nome = str(input('Nome do jogador: '))
desem['Nome'] = nome
npartidas = int(input(f'Quantas partidas {nome} jogou? '))

for c in range(0, npartidas):
    gols = int(input(f'Quantos gols na {c + 1}ª partida? '))
    dados.append(gols)
desem['Gols'] = dados[:]

r = 0
for g in dados:
    r += g
desem['Total'] = r
print('=-='*20)
print(desem)
print('=-='*20)
for k, v in desem.items():
    print(f'{k} = {v}')
print('=-='*20)
print(f'O jogador {nome} jogou {npartidas} partidas.')
for i, g in enumerate(dados):
    print(f' => Na {i+1}ª partida, fez {g} gols.')
print(f'Foi um total de {r} gols')