'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
(com idade) em um dicionario, se por acaso CTPS for diferente de zero, o dicionario recebera
tambem o ano de contrataçao e o salario. Calcule e acrescente, alem da idade com quantos anos a 
pessoa vai se aposentar.'''
from datetime import date
ano_atual = date.today().year
trabalhador = {}

trabalhador['Nome'] = str(input('Nome Completo: ')).strip().title()
trabalhador['Ano_Nascimento'] = int(input('Ano de Nascimento: '))
trabalhador['Idade'] = ano_atual - trabalhador['Ano_Nascimento']
trabalhador['Carteira_Trabalho'] = int(input('Digite os digitos da sua carteira de trabalho: [digite 0 se nao tiver] '))
if trabalhador['Carteira_Trabalho'] != 0:
    trabalhador['Ano_Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salario'] = float(input('Salario da época: R$'))
    trabalhador['Aposentadoria'] = trabalhador['Idade'] + (ano_atual - (trabalhador['Ano_Contratação'] + 35))
print('-=' * 30)
for k, v in trabalhador.items():
    print(f" - \033[1;32m{k}\033[m tem o valor de \033[1;32m{v}\033[m.")