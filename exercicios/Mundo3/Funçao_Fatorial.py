'''Crie um programa que tenha uma função fatorial() que receba dois parametros: o primeiro
que indique o numero a calcular e o outro chamado show, que sera um valor logico(opcional)
indicando se sera mostrado ou nao na tela o processo de calculo do fatorial.'''
from math import factorial

def fatorial(num, show=False):
    '''
    funcao para calcular o fatorial de qualquer numero, tendo opcao de mostrar ou nao
    a conta.
    num = numero para saber o fatorial;
    show = False para mostra apenas o resultado e True para mostra a conta.
    '''
    if show == True:
        fat = 1
        print(f"Calculando {num}! = ", end="")
        for c in range(num, 0, -1):
            print(f'{c}', end=" ")
            print(f'x ' if c > 1 else ' = ', end="")
            fat = fat * c
        print(fat, end="")
    else:
        return print(f'O fatorial de {num} é: {factorial(num)}')


numero = int(input('Quer ver o fatorial de qual numero? '))
fatorial(numero, show=True)
help(fatorial)