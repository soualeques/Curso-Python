'''Desenvolva um programa que leia o primeiro termo e a razao de uma PA,
no final mostre os 10 primeiros termos dessa progressão'''

termo = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
decimo_termo = termo + (10 - 1) * razao
for c in range(termo, decimo_termo + razao , razao):
    print(c, end= " -> ")
print("ACABOU!")