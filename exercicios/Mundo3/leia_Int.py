'''Crie um programa que tenha a funçao leiaInt(), que vai funcionar de forma semelhante
ao comando input(), so que fazendo a validaçao para aceitar apenas um valor numerico.'''


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mErro! Digite um numero inteiro valido.\033[m')
        if ok:
            break 
    return valor


#Programa principal
n = leiaInt('Digite um numero inteiro: ')
print(f'Voce acabou de digitar o numero: {n}')