'''Faça um programa que mostre varias informaoes sobre uma variavel'''
x = input("Digite alguma coisa: ")
print("o tipo primitivo é",type(x))
print('so tem espaço? ', x.isspace())
print('é um numero?', x.isnumeric())
print("esta tudo em minusculo?", x.islower)