from ex115 import *


def existearq(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Ouve um erro na criação do arquivo!')
    else:
        print('Arquivo .txt criado com sucesso!')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao tentar ler o arquivo')
    else:
        mensagem('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<38}{dado[1]:>5} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na escritura do dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()