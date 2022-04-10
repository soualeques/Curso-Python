'''Crie um programa que leia o nome e o preço de varios produtos. O programa
devera perguntar se o usuario vai continuar. No final mostre:
- Qual o total de gasto na compra.
- Quantos produtos custam mais de R$1.000,00
- Qual o nome do produto mais barato.'''

print('*-'*20)
print('{:^40}'.format('LOjAO DO ALEX'))
print('*-'*20)
total_compra = 0
compra_alta = 0
barato = " "
cont = 0
menor = 0
while True:
    nome_produto = str(input('NOME DO PRODUTO: ')).upper().strip()
    valor_produto = float(input('VALOR: R$ '))
    cont += 1 
    total_compra += valor_produto
    if valor_produto > 1000:
        compra_alta += 1
    if cont == 1:
        menor = valor_produto
        barato = nome_produto
    else:
        if valor_produto < menor:
            menor = valor_produto
            barato = nome_produto
    res = " "
    while res not in "SN":
        res = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if res == "N":
        break
print(f'Foi gasto o total de R${total_compra:,.2f}.')
print(f'Teve o total de {compra_alta} produtos custando mais de R$1.000,00.')
print(f'O produto mais barato foi {barato} que custa R${menor:,.2f}.')
print('{:-^40}'.format('FIM DO PROGRAMA'))