'''Escreva um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e menor
peso lido.'''

maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input(f'Digite o peso da {pessoa}º pessoa: (Kg)'))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior} e o menor foi {menor}')    