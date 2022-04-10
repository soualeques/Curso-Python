'''Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando 
o usuario digitar o valor 999, que é a condiçao de parada. No final mostre quantos numeros 
foram digitados e qual foi a soma entre eles (desconsiderando o flag com o BREAK).'''

cont = 0
soma = 0
while True:
    numero = int(input('Digite um valor, [digite 999 para parar]:  '))
    if numero == 999:
        print("Finalizando Programa...")
        break
    cont += 1
    soma = soma + numero
print(f'Foram digitados {cont} numeros e a soma entre eles foi de {soma}.')
print("----FIM DO PROGRAMA----")