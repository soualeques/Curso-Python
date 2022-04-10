'''Faça um programa que ajude um jogador da MEGA-SENA a criar palpites.
o programa deve perguntar quantos jogos serao feitos e vai sortear 6 numeros entre 1 a 60
para cada jogo, cadastrando em uma lista composta'''

from random import randint
from time import sleep

print('-=' * 20)
print('         MEGA SENA         ')
print('-=' * 20)

palpites = []
jogos = []

numero_palpites = int(input('Digite quantos palpites vai querer: '))
tot = 1
while tot <= numero_palpites:
    cont = 0 
    while True:
        num = randint(1, 60)
        if num not in palpites:
            palpites.append(num)
            cont += 1
        if cont >= 6:
            break
    palpites.sort()
    jogos.append(palpites[:])
    palpites.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {numero_palpites} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'JOGO {i + 1}: {l}')
    sleep(1)
print('-=' * 3 ,'BOA SORTE :)', '-=' * 3)
    