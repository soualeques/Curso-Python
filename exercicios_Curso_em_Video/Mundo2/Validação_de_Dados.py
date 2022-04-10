'''Faça um programa que leia o sexo de uma pessoa, mas so
aceite os valores 'M' ou 'F'. Caso esteja errado, peça a 
digitaçao novamente ate ter o valor correto.'''

sexo = str(input("Digite seu sexo: [M/F] ")).strip().upper()[0]
while sexo != "M" and sexo != "F":
    sexo = str(input("Dados invalidos!, Digite o sexo: [M/F]")).upper().strip()[0]
    
print(f"Cadastro do sexo {sexo} feito com sucesso!")