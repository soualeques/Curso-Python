'''Faça um mini sistema que utilize o interactive help do python, O usuario vai digitar o comando
e o manual vai aparecer. Quando o usuario digitar a palavra FIM, o programa se encerra.
OBS: use cores.'''
cores = (
    '\033[m',        # 0 Default
    '\033[0;30;41m', # 1 Vermelho
    '\033[0;30;42m', # 2 Verde
    '\033[0;30;43m', # 3 Amarelo
    '\033[0;30;44m', # 4 Azul
    '\033[0;30;45m', # 5 Roxo
    '\033[7;30m'     # 6 Branco
);

def consultar(txt):
    bonito('CONSULTANDO O MANUAL...', 4)
    print(cores[6], end="")
    help(txt)
    print(cores[0], end="")



def bonito(txt, cor=0):
    tam = len(txt) + 4
    print(cores[cor], end="")
    print('~' * tam)
    print(txt)
    print('~' * tam)
    print(cores[0], end="")





comando = ""
while True:
    bonito(' SISTEMA DE CONSULSTA ', 2)
    comando = str(input(' Digite uma função ou biblioteca: '))
    if comando.upper() == "FIM":
        break
    else:
        consultar(comando)
bonito('ATE MAIS...', 2)