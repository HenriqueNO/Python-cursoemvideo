from datetime import datetime
ano = datetime.now()

dados = {}
from datetime import date
dados['nome'] = str(input('Nome: '))
ADN = int(input('Ano de nacimento: '))
dados['idade'] = ano.year - ADN
dados['CTPS'] = int(input('Número da carteira de trabalho(0 não tem): '))
if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Informe seu salário: R$'))
    ap = 35 - (ano.year - dados['contratação'])
    dados['aposentadoria'] = dados['idade'] + ap

for k, v in dados.items():
    print(f'{k.upper()} = {v}')