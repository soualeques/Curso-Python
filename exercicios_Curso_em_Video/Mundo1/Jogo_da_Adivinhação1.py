'''Escreva um programa que faça o computador pensar em um numero
 inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual
 foi o numero escolhido pelo computador'''
 
import random
 
computador = random.randint(0,5)
usuario = int(input("Adivinhe o numero que estou pensando entre 0 e 5: "))
if computador == usuario:
    print("PARABENS!!! você acertou")
else:
    print("Voce errou!")