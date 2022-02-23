'''Reescreva a funçao leiaInt(), incluindo agora a possibilidade de digitaçao de um numero de tipo 
invalido, aproveite e crie tambem uma funçao leiaFloat() com a mesma funcionalidade '''

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


def leiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except:
            print('\033[1;31mErro Digite um numero valido\033[m')
            continue
        else:
            return f

#Programa principal
n = leiaInt('Digite um numero inteiro: ')
f = leiaFloat('Digite um numero real: ')
print(f'Voce acabou de digitar o numero: {n}, e o numero: {f}')