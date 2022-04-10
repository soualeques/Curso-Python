'''Crie um programa que leia varios numeros e coloque-os em uma lista.
Depois disso, mostre:
- Quantos numeros foram digitados;
- A lista de valores, em ordem decrescente;
- Se o valor 5 foi digitado e esta na lista.'''

lista_numeros = []
contador = 0
while True:
    numero = int(input('Digite um valor: '))
    lista_numeros.append(numero)
    contador += 1
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('Resposta invalida! Quer continuar? [S/N] ')).strip().upper()[0]
    if res == 'N':
        break
print("-_"*30)
if 5 in lista_numeros:
    print('O valor 5 esta presente na lista!')
else:
    print('O valor 5 não esta presente na lista!')
print(f'voce digitou {contador} numeros!')
lista_numeros.sort(reverse=True)
print(f'A lista em ordem decrescente fica: {lista_numeros}')