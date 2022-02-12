'''Faça um programa que leia 5 valores numericos e guarde-os em uma lista. No
final, mostre qual foi o menor e maior valor digitados e suas respectivas posições na lista.'''

valores = []
maior = menor = 0
for pos, v in enumerate(range(0, 5)):
    valores.append(int(input(f'digite um valor para posição {v}: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
    
print("-="*30)
print(f'voce digitou os valores: {valores}')
print(f'O maior valor digitado foi: {maior} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end="")
print(f'\nO menor valor digitado foi: {menor} nas posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end="")
