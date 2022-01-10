'''Faça um programa que jogue jokenpo com você'''

import random
from time import sleep

print('===='*8)
print('    JOKENPO    ')
print('===='*8)

escolha = int(input('''[0]PEDRA
[1]PAPEL
[2]TESOURA
sua escolha: '''))
print('\033[4;36mJO...\033[m')
sleep(1)
print('\033[4;36mKEN...\033[m')
sleep(1)
print('\033[4;36mPO!\033[m')


itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0,2)

print('==='*8)
print(f'O computador jogou {itens[computador]}')
print(f'Você jogou {itens[escolha]}')
print('==='*8)


#Computador jogou PEDRA.
if computador == 0:
    if escolha == 0:
        print('\033[1;33mEMPATE!\033[m')
    elif escolha == 1:
        print('\033[1;32mVOCE GANHOU!\033[m')
    elif escolha == 2:
        print('\033[1;31mVOCE PERDEU!\033[m')
#Computador jogou PAPEL.
elif computador == 1:
    if escolha == 0:
        print('\033[1;31mVOCE PERDEU!\033[m')
    elif escolha == 1:
        print('\033[1;33mEMPATE!\033[m')
    elif escolha == 2:
        print('\033[1;32mVOCE GANHOU!\033[m')
#Computador jogou TESOURA.
elif computador == 2:
    if escolha == 0:
        print('\033[1;32mVOCE GANHOU!\033[m')
    elif escolha == 1:
        print('\033[1;31mVOCE PERDEU!\033[m')
    elif escolha == 2: 
        print('\033[1;33mEMPATE!\033[m')
    
