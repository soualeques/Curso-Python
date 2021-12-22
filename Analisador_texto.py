"""Crie um programa que leia o nome de uma pessoa e analise da seguinte forma:
Colocar em maiusculo e minusculo
Contar quantas letras tem sem os espaços
Contar quantas letras tem o primeiro nome"""

nome = input("Digite seu nome completo: ")
nome_Maiusculo = nome.upper()
nome_Minusculo = nome.lower()
Contador_letras = len(nome.strip()) - nome.count(' ')
Cont_letras_primeiro_nome = nome.split()
print('nome em maiusculo: ', nome_Maiusculo)
print('nome em minusculo: ', nome_Minusculo)
print('numero de letras: ', Contador_letras)
print('numero de letras primeiro nome: ', len(Cont_letras_primeiro_nome[0]))