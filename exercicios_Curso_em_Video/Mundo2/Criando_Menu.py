'''Crie um programa que leia dois valores e mostre um menu fazendo as operaçoes de cada opção:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA'''
from time import sleep
print("\033[1;31mS2\033[m"*18)
print('\033[7;40m          CALCULADORA ALEX        \033[m')
print("\033[1;31mS2\033[m"*18)

valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))

escolha = 0

while escolha != 5 :
    escolha = int(input('''
\033[1;31m[1] SOMAR\033[m
\033[1;32m[2] MULTIPLICAR\033[m
\033[1;33m[3] MAIOR\033[m
\033[1;34m[4] NOVOS NUMEROS\033[m
\033[1;35m[5] SAIR DO PROGRAMA\033[m
sua escolha: '''))
    if escolha == 1:
        soma = valor1 + valor2
        print(f"A soma de \033[1;32m{valor1}\033[m e \033[1;32m{valor2}\033[m é \033[1;32m{soma}\033[m.")
    elif escolha == 2:
        multiplicação = valor1 * valor2
        print(f"A soma dos valores \033[1;32m{valor1}\033[m e \033[1;32m{valor2}\033[m é \033[1;32m{multiplicação}\033[m.")
    elif escolha == 3:
        if valor1 > valor2:
            print(f"O maior valor é \033[1;32m{valor1}\033[m.")
        else:
            print(f'O maior valor é \033[1;32m{valor2}\033[m.')
    elif escolha == 4:
        valor1 = int(input("Digite o novo valor: "))
        valor2 = int(input("Digite mais um valor: "))
    elif escolha == 5:
        print("FINALIZANDO PROGRAMA...")
        sleep(1.5)
    else:
        print("Opçao invalida")
        
print("-----PROGRAMA FINALIZADO-----")