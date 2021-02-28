s = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
while s not in 'MmFf':
    s = str(input('Dados inválidos! Por favor, informe seu sexo: ')).upper().strip()[0]
print('Sexo {} registrado'.format(s))