'''Crie um programa que tenha uma funçao chamada voto(), que vai receber como parametro
o ano de nascimento de uma pessoa, retornando um valor literal indicando se a pessoa pode votar, 
tem voto opcional (mais de 65 anos) ou nao pode votar.'''
from datetime import date

def voto(ano):
    idade = date.today().year - ano
    if idade >=16 and idade < 18:
        return print(f'com {idade} anos voce é Menor de idade mas tem: \033[1;33mVoto opcional!\033[m')
    if idade < 16:
        return print(f'com {idade}anos voce é Menor de idade: \033[1;32mNão vota\033[m')
    elif idade >= 18 and idade < 65:
        return print(f'com {idade} anos voce é Maior de idade: \033[1;31mVoto obrigatorio\033[m')
    else:
        return print(f'com {idade} anos voce é Idoso: \033[1;33mVoto opcional!\033[m')


def print_especial(txt):
    print('-=' * len(txt))
    print(f'{txt:^30}')
    print('-=' * len(txt))


print_especial('ANALISE SE PODE VOTAR')
ano_nascimento = int(input('Digite seu ano de nascimento: '))
voto(ano_nascimento)
