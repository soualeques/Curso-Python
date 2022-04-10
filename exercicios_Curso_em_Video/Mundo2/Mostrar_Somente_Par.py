'''Desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas 
daqueles que forem PAR, se for IMPAR, desconsiderar.'''

soma = 0
for c in range(0, 6):
    numero = int(input('Digite um numero inteiro: '))
    if numero % 2 == 0:
        soma = soma + numero
print(f"A soma dos numeros pares foi {soma}")