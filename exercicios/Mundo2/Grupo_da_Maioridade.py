'''Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre
quantas pessoas ainda nao atingiram a maioridade e quantas ja.'''

import datetime

ano_atual = datetime.date.today().year
total_maioridade = 0
total_menoridade = 0
for c in range(1, 8):
    nascimento = int(input(f"Digite o ano de nascimento da {c}º pessoa: "))
    idade = ano_atual - nascimento
    if idade >= 18:
        total_maioridade +=1
    else:
        total_menoridade +=1
print(f'Ao todo foram {total_maioridade} maiores de idade e {total_menoridade} menores de idade!')