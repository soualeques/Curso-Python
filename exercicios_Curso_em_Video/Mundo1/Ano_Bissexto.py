'''Faça um programa que leia um ano qualquer e mostre se ele é Bissexto'''

from datetime import date

ano = int(input("Que ano quer analisar? Digite 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"\033[7;40m{ano} é um ano BISSEXTO!\033[m")
else:
    print(f"\033[1;31;44m{ano} nao é um ano BISSEXTO!\033[m")