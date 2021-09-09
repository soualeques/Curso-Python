#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto#
produto = float(input("Qual o preço do produto? R$"))
desconto = produto * 5 / 100
print("O preço do produto com 5% de desconto fica: R${}".format(desconto))