'''Escreva um programa que pergunte o sálario de um funcionario e calcule o valor do seu
aumento.
Para salarios superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais. o aumento é de 15%.'''

salario = float(input("Digite o salario do funcionario: R$"))
if salario <= 1250:
    novosalario = salario + (salario * 0.15)
if salario > 1250:
    novosalario = salario + (salario * 0.10)
    
print(f"O aumento do salario do funcionario sera de R$\033[1;32m{novosalario:,.2f}\033[m")