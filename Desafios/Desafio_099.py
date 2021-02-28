def maior(*num):
    print('--' * 20)
    print(f'Analisando os valores passados...')
    for n in num:
        print(f'{n} ', end='')
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'o maior valor informado foi {max(num)}')
    print('--'*20)

maior(2, 4, 7, 3, 6)
maior(1, 2, 3, 4, 5, 5, 6, 7,)
maior(2, 1)
