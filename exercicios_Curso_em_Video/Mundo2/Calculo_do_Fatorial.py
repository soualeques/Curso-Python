'''Faça um programa que leia um numero qualquer e faça seu fatorial'''

#METODO 1 (BIBLIOTECA)
'''from math import factorial
numero = int(input("Digite um numero para ver seu fatorial: "))
fatorial = factorial(numero)
print(f'O fatorial de {numero} é {fatorial}.')'''

#METODO 2 (REPETIÇÃO WHILE)
'''numero = int(input("Digite um numero para ver seu fatorial: "))
c = numero
fatorial = 1
print(f"Calculando {numero}! = ", end="")
while c > 0:
    print(f'{c}', end=" ")
    print(f'x ' if c > 1 else ' = ', end="")
    fatorial = fatorial * c
    c = c - 1
print(f"{fatorial}")'''

#METODO 3 (REPETIÇÃO FOR)
numero = int(input("Digite um numero para saber seu fatorial: "))
fatorial = 1
print(f"Calculando {numero}! = ", end="")
for c in range(numero, 0, -1):
    print(f'{c}', end=" ")
    print(f'x ' if c > 1 else ' = ', end="")
    fatorial = fatorial * c
print(f'{fatorial}')
    