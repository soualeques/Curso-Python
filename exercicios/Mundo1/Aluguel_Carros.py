'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos quais foi alugado. Calcule o preço a pagar, sabendo
que o carro custa R$60 por dia e R$0,15 por Km rodado'''

Km = float(input("Km percorrido pelo carro: "))
dias = int(input("Dias alugado: "))
custo = dias * 60 + Km * 0.15
print("O valor do aluguel pelo carro fica em \033[0;31mR${:.2f}\033[m".format(custo))