'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
retangulo. calcule e mostre o comprimento da hipotenusa'''
from math import hypot
Co = float(input("Digite o cateto oposto: "))
Ca = float(input("Digite o cateto adjascente: "))
print("O valor da hipotenusa de {} e {} é {}".format(Co,Ca,hypot(Co,Ca)))