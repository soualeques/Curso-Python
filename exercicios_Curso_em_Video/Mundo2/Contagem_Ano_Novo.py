'''Faça um program que mostre uma contagem regressiva para os estouros de fogos de artificil.
indo de 10 ate 0 com pausa de 1 segundo entre eles.'''
from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[1;36;40mFELIZ ANO NOVO MEUS QUERIDOS!\033[m')