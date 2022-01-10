'''Desenvolva um programa que leia um numero inteiro e diga se ele é primo ou nao'''

numero = int(input("Digite um numero: "))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[31m', end=" ")
        tot += 1
    else:
        print('\033[32m', end=" ")
    print(c, end=" ")
print(f"\n\033[mO numero {numero} foi divisil {tot} vezes")
if tot == 2:
    print("E por isso ele é primo")
else:
    print('E por isso ele nao é primo')
    
        