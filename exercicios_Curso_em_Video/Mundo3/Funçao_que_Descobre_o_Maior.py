'''Faça um programa que tenha uma função chamada maior(), que receba varios parametros com
valores inteiros. seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep

def maior(*num):
    mai = cont = 0
    print('-=' * 20)
    print("Analisando os valores...")
    for valor in num:
        print(f'{valor} ', end="", flush=True)
        sleep(0.5)
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
    print(f"\nForam analisados {cont} valor(es).")
    print(f'O maior valor foi: {mai}')
    
    
    
#programa principal
maior(1, 5, 6, 7, 19)
maior(2, 4, 5, 6,13,42)
maior(4,7)
maior(4)    
    