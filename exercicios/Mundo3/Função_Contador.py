'''Faça um programa que tenha uma funçao chamada contador(), que receba tres parametros:
inicio, fim e passo. Seu programa tem que realizar tres contagens atraves da função criada:
- De 1 ate 10 de 1 em 1;
- De 10 ate 0, de 2 em 2;
- Uma contagem personalizada.'''
from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    sleep(1.5)
    if passo < 0:
        passo *= 1
    if passo == 0:
        print('ERRO! a contagem sera de 1 em 1.')
        passo = 1
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end="", flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end="", flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')
    

#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print(' agora Contagem personalizada...')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)