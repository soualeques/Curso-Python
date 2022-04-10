'''Escreva um programa que leia um numero n inteiro qualquer e  mostre na tela os n primeiros
elementos de uma sequencia de fibonacci.'''

print("-"*29)
print("    SEQUENCIA DE FIBONACCI")
print("-"*29)

n = int(input("Quantos termos voce quer ver? "))
t1 = 0
t2 = 1
print("~"*29)
print(f'{t1} -> {t2} -> ', end=" ")
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f"{t3} -> ", end="")
    t1 = t2
    t2 = t3
    cont += 1 
print(" FIM")
print("~"*29)

