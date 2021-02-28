nome: str = input('Qual é o seu nome?').strip()
print('Olá {}{}{}! É um prazer te conhecer!'.format('\033[1;34m', nome, '\033[m'))