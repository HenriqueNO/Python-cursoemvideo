time = ('Palmeiras', 'Flamengo', 'Internaciona', 'Grêmio',
        'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro',
        'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians',
        'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná')
print(f'Lista dos times do Brasileirão: {time}')
print('=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=---=--')
print(f'Primeiros cinco times: {time[:5]}')
print('=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=---=--')
print(f'Os quatro ultimos são: {time[-4:]}')
print('=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=---=--')
print(f'Times em ordem alfabetica: {sorted(time)}')
print('=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=---=--')
print(f'Posiçao do time Chapecoense: {time.index("Chapecoense") + 1}ª posição')