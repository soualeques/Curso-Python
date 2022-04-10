'''Faça um programa que leia o nome e peso de varias pessoas, no final mostre:
- Quantas pessoas foram cadastradas;
- Uma listagem com as pessoas mais pesadas;
- Uma listagem com as pessoas mais leves.'''

from pkg_resources import ensure_directory


temp = []
principal = []
totpessoas = 0
maior = menor = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    temp.append(nome)
    temp.append(peso)
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()
    totpessoas += 1
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if res == 'N':
        break
print('-='*30)
print(f'Foram cadastradas ao total {totpessoas} pessoa(s)...')
print(f'O maior peso foi {maior}Kg de ', end="")
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}')
print()
print(f'O menor peso foi {menor}Kg de ', end="")
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}')
print()