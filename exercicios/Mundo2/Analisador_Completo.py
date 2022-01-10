'''Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 pessoas. No final do programa, mostre:
- a media do grupo
- qual o nome do homem mais velho
- quantas mulheres temm menos de 20 anos.'''

somaidade = 0
maisvelho = " "
mulher_menoridade = 0
homem_maioridade = 0
for c in range(1, 5):
    print(f"---- {c}º PESSOA ----")
    nome = str(input('NOME: '))
    idade = int(input('IDADE:'))
    sexo = str(input("SEXO: [M/F] ")).strip().upper()
    if sexo == "F" and idade < 20:
        mulher_menoridade = mulher_menoridade +1
    somaidade = somaidade + idade
    if c == 1 and sexo == "M":
        maisvelho = nome
        homem_maioridade = idade
    if idade > homem_maioridade and sexo == "M":
        maisvelho = nome
        homem_maioridade = idade
        
    
media = somaidade / 4
print(f'A media das idades das pessoas é de \033[1;32m{media:,.2f}\033[m')
print(f"foram cadastradas \033[1;32m{mulher_menoridade}\033[m mulheres com menos de 20 anos.")
print(f'O nome do homem mais velho é \033[1;32m{maisvelho}\033[m.')    