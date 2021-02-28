def notas(*resp, show=False):
    """
    -> A função cadastra as notas dos alunos em um dicionario e apresenta a situação de varios alunos.
    :param resp: Notas a cadatrar, não tem limite
    :param show: Show=True, para mostrar a situação geral dos alunos.
    :return: retorna os valores em um dicionario.
    """
    mai = max(resp)
    men = min(resp)
    cont = 0
    n = 0
    a = 0
    for n in resp:
        a += n
        cont += 1
    media = a / cont
    resp = {'Total': cont, 'Maior': mai, 'Menor': men, 'Média': media}
    if show:
        media = int(media)
        if media >= 7:
            resp['Situação'] = 'Boa'
        elif media < 5:
            resp['Situação'] = 'Ruim'
        elif 5 >= media < 7:
            resp['Situação'] = 'Razoável'
    return resp


# Programa principal
resp = notas(5.5, 10, 2, show=True)
print(resp)