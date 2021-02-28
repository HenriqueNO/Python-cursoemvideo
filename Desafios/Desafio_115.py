import ex115
from time import sleep
import arquivo

arq = 'CEV.txt'

if arquivo.existearq(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado')
    arquivo.criararquivo(arq)


while True:
    mr = ex115.menu(['Ver dados de pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair do menu'])

    if mr == 1:
        arquivo.lerarquivo(arq)
    elif mr == 2:
        ex115.mensagem('NOVO CADASTRO')
        nome = str(input('Nome: ')).lower().strip().capitalize()
        idade = ex115.leiaint('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif mr == 3:
        ex115.mensagem('Saindo do sistema!')
        break
    sleep(1.5)