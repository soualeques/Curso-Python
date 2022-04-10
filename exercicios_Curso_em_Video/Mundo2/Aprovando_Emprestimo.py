'''Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa.
Pergunte o VALOR DA CASA, o SALARIO do comprador e em QUANTOS ANOS ele vai pagar.
A prestação mensal, nao pode exceder 30% do salario ou entao o emprestimo sera negado.'''

valor_casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite seu salario: R$"))
tempo = int(input("Em quantos anos pretende pagar? "))

#Calcular prestação multilplicando os anos por 12 para ter os meses.
prestaçao = valor_casa / (tempo * 12)

#Calcular se o salario excede os 30%
minimo = salario * 30 / 100

print(f"Com o salario de R${salario:,.2f}, voce teria de pagar prestações mensais de R${prestaçao:,.2f} durante {tempo} anos \nEntao:")
if prestaçao <= minimo:
    print("\033[1;32mEmprestimo Aprovado!\033[m")
else:
    print("\033[1;31mEmprestimo Negado!\033[m")
