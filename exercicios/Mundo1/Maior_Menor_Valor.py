'''Faça um programa que leia tres numeros e mostre
qual é o maior e qual o menor'''

numero1 = int(input("Digite um valor: "))
numero2 = int(input("Digite outro valor: "))
numero3 = int(input("Digite mais um valor: "))

#Verificando o numero menor
if numero1 < numero2 and numero1 < numero3:
    menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
    
#Verificando o numero maior
if numero1 > numero2 and numero1 > numero3:
    maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3
    
print(f"O maior valor digitado foi {maior}, e o menor foi {menor}.")