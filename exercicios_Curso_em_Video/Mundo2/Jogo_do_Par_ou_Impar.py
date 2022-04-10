''''Faça um programa que jogue PAR ou IMPAR com o computador. o jogo so
sera interrompido quando o jogador perder, mostrando o total de vitorias
consecutivas que ele conquistou no final do jogo.'''

from random import randint
from time import sleep

soma = 0
vitorias = 0

print('-#-#-'*9)
print('\033[1;35m        JOGO DO PAR OU IMPAR       \033[m')
print('-#-#-'*9)

while True:
    numero_jogador = int(input('Digite um numero: '))
    numero_computador = randint(0, 10)
    soma = numero_computador + numero_jogador
    escolha_jogador = " "
    while escolha_jogador not in "PI":
        escolha_jogador = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print('\033[1;35mPAR\033[m')
    sleep(0.5)
    print('\033[1;34mOU\033[m')
    sleep(0.5)
    print('\033[1;33mIMPAR...\033[m')
    sleep(0.5)
    print('-#-#-'*9)
    print(f"Voce jogou {numero_jogador}, e o computador {numero_computador}\nque deu: {soma}")
    print('-#-#-'*9)
    
    if escolha_jogador == "P":
        if soma % 2 == 0:
            print('\033[1;32mDEU PAR!...Voce venceu\033[m')
            print('\033[1;33mBOA...VAMOS MAIS UMA VEZ\033[m')
            vitorias += 1
        else:
            print('\033[1;31mDEU IMPAR!...Voce perdeu\033[m')
            break
    elif escolha_jogador == "I":
        if soma % 2 == 1:
            print('\033[1;32mDEU IMPAR!...Voce venceu\033[m')
            print('\033[1;33mBOA...VAMOS MAIS UMA VEZ\033[m')
            vitorias += 1
        else:
            print('\033[1;31mDEU PAR!...Voce perdeu\033[m')
            break
print('\033[4;33m-#-#-\033[m'*9)
print(f'Fim do jogo... com total de \033[1;32m{vitorias}\033[m vitorias consecutivas!')
print('\033[4;33m-#-#-\033[m'*9)

        
    
            
