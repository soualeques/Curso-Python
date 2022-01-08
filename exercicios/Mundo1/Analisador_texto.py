"""Crie um programa que leia o nome de uma pessoa e analise da seguinte forma:
Colocar em maiusculo e minusculo
Contar quantas letras tem sem os espaços
Contar quantas letras tem o primeiro nome"""

nome = input("Digite seu nome completo: ")
nome_Maiusculo = nome.upper()
nome_Minusculo = nome.lower()
Contador_letras = len(nome.strip()) - nome.count(' ')
Cont_letras_primeiro_nome = nome.split()
print(f'nome em maiusculo: \033[1;32;41m{nome_Maiusculo}\033[m')
print(f'nome em minusculo: {nome_Minusculo}\033[m')
print(f'numero de letras:  {Contador_letras}\033[m]')
print(f'numero de letras primeiro nome:  \033[4;32m{len(Cont_letras_primeiro_nome[0])}\033[m')