'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno
e tangente desse ângulo'''
from math import tan,sin, cos, radians
ang = float(input("Digite um ângulo qualquer: "))
print('Com o ângulo de {}º temos... \n seno = {:.2f} \n cosseno = {:.2f} \n tangente = {:.2f}'.format(ang, sin(radians(ang)), cos(radians(ang)),tan(radians(ang))))