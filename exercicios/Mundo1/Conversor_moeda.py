#Faça um programa que converta moeda Real para Dolar#
dinheiro = float(input('Quantos dinheiro voce tem na carteira? R$'))
dolar = dinheiro / 5.17
print("com esse valor voce teria ${:.2f} dolars na carteira ".format(dolar))