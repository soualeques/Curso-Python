'''Melhore o exercio Jogo_da_Adivinhação, onde o computador vai 'pensar' em um numero entre
0 e 10. so que agora o jogador vai tentar adivinhar ate acertar, mostrando no final
quantos palpites foram necessarios.'''
 
from random import randint

computador = randint(0,10)
contagem_palpites = 1
print("==#=="*10)
print("\033[4;31m           JOGO DA ADIVINHAÇÃO      \033[m")
print("==#=="*10)

jogador = int(input("Sou seu computador, estou pensando em um numero entre 0 e 10 \ntente adivinhar qual é, seu palpite: "))
while jogador != computador:
    if computador > jogador:
        jogador = int(input("\033[1;31mMais!, tente denovo:\033[m "))
        contagem_palpites += 1
    elif computador < jogador:
        jogador = int(input("\033[1;31mMenos! tente denovo:\033[m "))
        contagem_palpites += 1
print("\033[1;32mVOCÊ ACERTOU! PARABENS!\033[m")
print(f"Você fez \033[1;32m{contagem_palpites}\033[m palpites.")
