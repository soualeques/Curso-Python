import urllib.request
import urllib

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except: 
    print('O site esta indisponivel no momento')
else:
    print('O site esta acessivel')
    print(site.read()) #mostra HTML do site
finally:
    print('Obrigado por usar meu programa')
    