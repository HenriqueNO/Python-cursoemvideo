#Dicionarios

#Formas de usar as chaves:
#dados = disct()
#dados = {}

dados = {'nome': 'Henrique', 'idade': 17} #Estruturas das chaves
print(dados['nome']) #Printa o dado 'nome'
print(dados['idade']) #Printa o dado 'idade'

dados['Sexo'] = 'Masculino' #Adicionar um elemento
print(dados['Sexo'])

del dados['idade'] #deletar um elemento

print(dados.values()) #Printa todos dos valores
print(dados.keys()) #Printa todas as chaves
print(dados.items()) #Printa todos os elementos do dicionario

for k, v in dados.items(): #Printa de forma bonita
    print(f'O {k} é {v}')

Banco = [dados, {'Nome': 'Nunes', 'Sexo': 'Masculino'}]  #Dicionario dentro de chave
print(Banco[1]['Nome']) #printando um dado do dicionario que esta dentro da lista

for d in Banco: #Print bonito do dicionario dentro da lista.
    for k, v in d.items():
        print(f'O {k} é {v}')