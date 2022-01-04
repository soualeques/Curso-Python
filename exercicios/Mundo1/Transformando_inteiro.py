#Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira#
from math import trunc
num = float(input("Digite um numero Real: "))
print("A parte inteira de {} é {}".format(num, trunc(num)))