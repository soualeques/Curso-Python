'''Crie um programa que leia varios numeros e coloque-os em uma lista, depois
crie outras duas lista para os numeros pares e impares.
Ao final mostre as tres listas.'''
lista_numeros = []
numeros_pares = []
numeros_impares = []

while True:
    numero = int(input('Digite um valor: '))
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while res not in "SN":
        res = str(input('Resposta Invalida! Quer continuar? [S/N] ')).strip().upper()[0]
    if res == "N":
        break
    lista_numeros.append(numero)
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
print('-_'*30)
print(f'A lista completa ficou assim: {lista_numeros}')
print(f'A lista com numeros pares ficos assim: {numeros_pares}!')
print(f'A lista com numeros impares ficou assim: {numeros_impares}!')
