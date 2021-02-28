sexo = str(input('Você é homem ou mulher? ')).strip().lower()

#ano = int(input('Informe o ano em que nasceu: '))
#conta= 2019 - ano
#print('Você tem {} anos'.format(conta))
if sexo == 'homem':
    ano = int(input('Informe o ano em que nasceu: '))
    conta = 2019 - ano
    print('Você tem {} anos'.format(conta))
    if conta > 18:
        faz = conta - 18
        print('O tempo de alistamento ja passou, e ja faz {} ano(s)'.format(faz))
        print('Seu alistamento foi em {}'.format(2019 - faz))
    if conta < 17:
        falta = 18 - conta
        print('O tempo de alistamento ainda não passou, e falta {} ano(s)'.format(falta))
        print('Seu alistamento será em {}'.format(2019 + falta))
    if conta == 18 or 17:
        print('Esta na hora de se apresentar para o alistamento!')
else:
    print('Sendo mulher o alistamento nao é obrigatorio')