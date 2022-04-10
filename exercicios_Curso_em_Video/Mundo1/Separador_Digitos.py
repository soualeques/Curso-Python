"""Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um 
dos digitos separados."""

num = int(input("Digite um numero: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f"Analisando numero {num}...")
print(f"esse numero tem {u} unidades.")
print(f"esse numero tem {d} dezenas.")
print(f"esse numero tem {c} centenas.")
print(f"esse numero tem {m} milhares.")