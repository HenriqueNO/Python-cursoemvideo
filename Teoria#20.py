# Transformando rotinas em funções no python.


# def mostralinha(): # criando uma linha em função
  #  print('--------------------------------------------')


# def mensagem(msg): # criando uma função com 2 linhas e uma mensagem no meio
 #   print('==='*25)
 #   print(msg)
 #   print('==='*25)


# programa principal
# mostralinha()
# print()
# mensagem('Olá')


# def soma(a, b):
    # s = a + b
    # print(s)


#soma(1, 2)      # rodando a função
#soma(a=1, b=2)  # explicitando qual é A e qual é B

# def contador(* num):  # Empacotador
#    print(num)


# contador(1, 2, 3, 4)
# contador(1, 2)
# contador(10)


def dobra(lis):  # função para dobrar valores de uma lista
    pos = 0
    while pos < len(lis):
        lis[pos] *= 2
        pos += 1
    print(lis)


valores = [2, 3, 5, 6]
print(valores)
dobra(valores)

