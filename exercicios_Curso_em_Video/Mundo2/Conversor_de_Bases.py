'''Escreva um programa que leia um numero inteiro qualquer e peça 
para o usuario escolher qual sera a base de conversao:
1- para BINARIO
2- para OCTAL
3- para HEXADECIMAL'''

numero = int(input("Digite um numero inteiro qualquer: "))
base = int(input('''Escolha uma das bases para conversao:
                 [1] para BINARIO
                 [2] para OCTAL
                 [3] para HEXADECIMAL
                 sua opção: '''))

if base == 1:
    print("o numero {} em BINARIO fica \033[4;31m{}\033[m".format(numero, bin(numero)[2:]))
    #Coloca [] depois da variavel para fatiar.
elif base == 2:   
    print(f"o numero{numero} em OCTAL fica \033[4;31m{oct(numero)[2:]}\033[m")
elif base == 3:
    print(f"o numero {numero} em HEXADECIMAL fica \033[4:31m{hex(numero)[2:]}\033[m")