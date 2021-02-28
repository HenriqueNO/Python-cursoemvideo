import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print('Não foi possivel acessar o site ')
else:
    print('O site esta acessivel')