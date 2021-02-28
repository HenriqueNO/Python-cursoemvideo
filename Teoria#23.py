# Tratamento de erros e exceções

try:      # Tente
    a = int(input('Numerador: '))
    b = int(input('Denominardor: '))
    r = a / b

except KeyboardInterrupt:
    print('O usuario não informou os dados')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero')

except Exception as erro:   # Falhou
    print(f'Infelizmente tivemos um problema conhecido como \033[1m({erro.__cause__})\033[m')

else:     # Deu certo
    print(f'O resultado é {r:.2f}')

finally:  # Indepedente de certo/falha
    print('Obrigado, volte sempre!')
