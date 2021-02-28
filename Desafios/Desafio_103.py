def ficha(nome='', gols=0):
    print('-=-'*20)
    print(f'{" -- Apresentado os dados do jogador --":>45}')
    if nome == '':
        print('Jogador: Desconhecido')
    else:
        print(f'Jogador: {nome}')
    if gols != 0:
        print(f'Gol(s) no campeonato: {gols}')
    else:
        print('Gol(s) no campeonato: 0')
    print('-=-'*20)


print('-- Preencha com os dados do jogador --')
nome = str(input('Nome do jogador: '))
gols = (input('Total de gol(s) do jogador: '))
if gols == '':
    gols = int(0)
else:
    gols = int(gols)

ficha(nome, gols)