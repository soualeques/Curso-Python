'''Crie um programa que tenha uma tupla com varias palavras(nao usar acento), depois disso, voce 
devera mostrar para cada palavra quais sao suas vogais'''

palavras = ('agua', 'ventilador', 'sabonete', 'dormir', 'lixo','computador', 'usuario','mentira')

for p in palavras:
    print(f'\nNa palavra \033[1;32m{p.upper()}\033[m temos as seguintes vogais: ', end=" ")
    for letra in p:
        if letra.lower() in "aeiou":
            print(f"\033[1;32m{letra}\033[m", end=" ")