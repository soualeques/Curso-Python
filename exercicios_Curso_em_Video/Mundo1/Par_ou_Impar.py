'''Crie um programa que leia um numero inteiro e diga se ele
é PAR ou IMPAR'''

numero = int(input("Digite um numero para saber se ele é par ou impar: "))
if numero % 2 == 0:
    print("Esse numero é PAR!")
else:
    print("Esse numero é IMPAR!")