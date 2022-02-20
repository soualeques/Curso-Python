'''Faça um programa que tenha uma lista chamada numeros e duas funçoes chamadas sorteia() e somaPar().
A primeira funçao vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda funçao vai
mostrar a soma entre todos os valores pares sorteados pela funçao anterios.'''
from random import randint
from time import sleep



def sorteia(lista):
    print('-='* 30)
    print('A lista de numeros sorteados foi: ', end="", flush=True)
    for v in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'\033[1;33m{n}\033[m ', end="", flush=True)
        sleep(0.5)
    


def SomaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'\nA soma dos numeros pares é: \033[1;33m{soma}\033[m')
    print('-=' * 30)


numeros = []
sorteia(numeros)
SomaPar(numeros)
            
        
        