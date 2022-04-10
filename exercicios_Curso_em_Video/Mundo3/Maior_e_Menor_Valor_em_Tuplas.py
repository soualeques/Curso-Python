'''Crie um programa que gere 5 numeros aleatorios e colocar em uma tupla. 
Depois disso mostre a listagem dos numeros gerados e tambem indique o maior
e menor valor'''

import random
numeros = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
print('Os valores sortedos foram: ')
print(numeros)
print(f'O maior valor foi: {max(numeros)}')
print(f'O menor valor foi: {min(numeros)}')