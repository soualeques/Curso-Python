'''Crie um programa que tenha uma tupla com nomes de produtos e seus respectivos preços
na sequencia. No final, mostre uma listagem de preços, organizando os dados em forma tabular'''

listagem = ("Agua", 2,
            "Coca-Cola",4.50,
            "Coca-Cola 2L", 9,
            "Salgadinho", 5,
            "Chocolate", 4.50,
            "Bala", 0.50,
            "Iorgute", 2.50,
            "Coxinha", 4)

print("-*"*20)
print(f'{"MERCADINHO DO ALEX":^30}')
print("-*"*20)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end="")
    else:
        print(f'R${listagem[pos]:>7.2f}')