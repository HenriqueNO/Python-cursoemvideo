jogador = {}
partidas = []
time = []
p = ''
dados = 0

while p != 'n':
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        p = str(input('Quer adicionar mais algum jogador? [S/N]: ')).lower().strip()[0]
        if p in 'sn':
            break
        else:
            print('Valor inválido! Por favor digite apenas S ou N.')


print('-=-' * 15)
print(time)
print('-=-' * 15)

print(' Cod Nome             Gols            Total')
print('---' * 15)

for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<17}', end='')
    print()
while True:
    while True:
        print('---' * 15)
        dados = int(input('Mostrar dados de qual jogador? '))
        if dados >= 0 and dados <= len(time) - 1:
            break
        elif dados == 999:
            break
        else:
            print('Cod inválido! Por favor tente novamente. ')
    if dados == 999:
        break
    print(f'-- Levantamento do jogador {time[dados]["nome"].upper()} --')
    for i, d in enumerate(time[dados]['gols']):
        print(f'   No JOGO {i + 1} fez {d} GOLS')
print('-=-' * 15)
print('<< Processo finalizado >>')