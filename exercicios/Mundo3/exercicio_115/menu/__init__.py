from time import sleep

ca = (
    '\033[m',        # 0 Default
    '\033[0;30;41m', # 1 Vermelho  
    '\033[0;30;42m', # 2 Verde
    '\033[0;30;43m', # 3 Amarelo
    '\033[0;30;44m', # 4 Azul
    '\033[0;30;45m', # 5 Roxo
    '\033[7;30m'     # 6 Branco
)
cl = (
    '\033[m',       # 0 Default
    '\033[0;31m', # 1 Vermelho  
    '\033[0;32m', # 2 Verde
    '\033[0;33m', # 3 Amarelo
    '\033[0;34m', # 4 Azul
    '\033[0;35m', # 5 Roxo
)


def men(txt):
    print('-' * len(txt)) 
    print(f'{cl[3]}{txt}{cl[0]}')
    print('-' * len(txt))
    
def escolhas(msg):
 while True:   
    sleep(1.5)
    men('           MENU PRINCIPAL          ')
    print(f'''{cl[4]}1 - CADASTRAR NOVA PESSOA
2 - VISUALIZAR PESSOAS CADASTRADAS
3 - SAIR{cl[0]}''')
    print('-' * 35)
    try:
            f = int(input(msg))
    except:
            print('\033[1;31mErro Digite um numero valido\033[m')
            continue
    else:
            if f == 1:
                print('pessoa cadastrada')
            elif f == 2:
                print('pessoas sao:...')
            elif f == 3:
                print('Saindo do programa...')
                sleep(1)
                break
            else:
                 print('{cl[1]}Nao tem essa escolha!{cl[0]}')
    