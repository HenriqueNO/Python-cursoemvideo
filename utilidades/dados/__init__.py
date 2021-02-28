def leiadinheiro(v):
    valido = False
    while not valido:
        entrada = str(input(v)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '.' or entrada == '':
            print(f'\033[1;31mERRO: "{entrada}" é um preço inválido\033[m')
        else:
            valido = True
            return float(entrada)


