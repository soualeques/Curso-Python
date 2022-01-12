'''Crie um programa que leia varios numeros inteiros pelo teclado.
O programa so vai parar quando o usuario digitar '999', que é a condiçao
de parada. No final mostre  quantos numeros foram digitados e qual a soma 
entre eles (descosiderando o flag).'''

numero = 0
cont = 0
soma = 0
numero = int(input('Digite um numero: [999 para parar] '))
while numero != 999:
    cont = cont + 1
    soma = soma + numero
    numero = int(input('Digite um numero: [999 para parar] '))
print(f"foram digitados {cont} numeros e a soma deu {soma}")
    