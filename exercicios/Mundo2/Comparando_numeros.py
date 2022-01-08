'''Escreva um programa que leia DOIS NUMEROS inteiros e compare-os, mostrando na tela uma mensagem:
O primeiro numero é maior se for
O segundo numero é maior se for
Se nao tiver maior, os numeros sao iguais.'''

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 > numero2:
    print(f"O primeiro numero \033[1;32;40m{numero1}\033[m é maior!")
elif numero2 > numero1:
    print(f"O segundo numero \033[1;32;40m{numero2}\033[m é maior!")
elif numero1 == numero2:
    print("Ambos os numeros sao iguals!")