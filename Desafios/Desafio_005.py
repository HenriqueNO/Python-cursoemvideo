print('=-='*12,'\033[1;36mdesafio005', '\033[m=-='*12)
print('\033[1;36m-=-'*6, 'Digite um valor e veja seu \033[1;31mANTERIOR\033[m \033[1;36me \033[1;31mSUCESSOR\033[m','\033[1;36m-=-'*6)
n1 = int(input('\033[m                                          ' ))
from time import sleep
print('\033[1;33m                                 ...PROCESSANDO...\033[m')
sleep(1)
print('=-='*28)
#Ant = n1 - 1
#Suc = n1 + 1
print('    Seu \033[1;31mnúmero digitado\033[m foi \033[1;34m{}\033[m, o número \033[1;31manterior\033[m a ele é \033[1;34m{}\033[m e seu \033[1;31msucessor\033[m é \033[1;34m{}\033[m'.format(n1,n1 - 1,n1 + 1) )
print('=-='*28)