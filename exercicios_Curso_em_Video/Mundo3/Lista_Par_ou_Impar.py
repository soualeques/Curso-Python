'''Crie um programa que leia 7 valores e cadastre-os em uma lista unica que mantenha separados
os numeros pares e impares. No final mostre os valores pares e impares em ordem crescente.'''

numeros = [[],[]]

for c in range(1, 8):
    valor = int(input(f'{c}º Valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-='*30)
print(f'Os valores pares são: \033[1;32m{sorted(numeros[0])}\033[m')
print(f'Os valores impares são: \033[1;31m{sorted(numeros[1])}\033[m')