'''Crie um programa que leia o nome, sexo e idade de varias pessoas, guardando os dados de
cada pessoa em um dicionario e todos os dicionarios em uma lista. No final, mostre:
- Quantas pessoas cadastradas;
- A media de idade;
- Uma lista de mulheres;
- uma lista com idade acima da media.'''

pessoas = {}
grupo = []
mulheres = []
acima = [] 
media = soma = 0
while True:
    pessoas['Nome'] = str(input('Nome:')).strip().title()
    pessoas['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while pessoas['Sexo'] not in "MF":
        pessoas['Sexo'] = str(input('Digito errado! Sexo [M/F]: ')).strip().upper()[0]
    if pessoas['Sexo'] == "F":
        mulheres.append(pessoas['Nome'])
    pessoas['Idade'] = int(input('Idade: '))
    grupo.append(pessoas.copy())
    soma += pessoas['Idade']
    media = soma / len(grupo)
    res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('Erro de digitaçao! Quer continuar? [S/N]: ')).strip().upper()[0]
    if res == "N":
        break
print('-=' * 30)
print(f'A) Foram cadastradas o total de \033[1;31m{len(grupo)}\033[m pessoa(s)!')
print(f'B) A média de idade das pessoa(s) é de: \033[1;31m{media:,.2f}\033[m')
print(f'C) A(s) mulher(es) cadastrada(s) foram: \033[1;31m{mulheres}\033[m')
print(f'D) A(s) pessoa(s) acima da média de idade é: ', end="")
for c in grupo:
    if c['Idade'] >= media:
        print(f'\033[1;31m{c["Nome"]}\033[m')
print('-=' * 30)

