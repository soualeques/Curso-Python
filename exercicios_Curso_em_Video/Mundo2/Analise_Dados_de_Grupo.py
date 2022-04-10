'''Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada o programa
deve perguntar se quer continuar ou nao, no final mostre:
- Quantas pessoas tem mais de 18 anos;
- Qauntos homens foram cadastrados;
- Quantas mulheres tem menos de 20 anos.'''

total_homens = 0
maior_idade = 0
mulheres_menos_vinte = 0
while True:
    print('*'*20)
    print('\033[1;34mCADASTRO DE PESSOAS\033[m')
    print('*'*20)
    idade = int(input('IDADE: '))
    if idade > 18:
        maior_idade +=1
    sexo = " "
    while sexo not in "MF":
        sexo = str(input('SEXO: [M/F] ')).upper().strip()[0]
    if sexo == "M":
        total_homens += 1
    if sexo == "F" and idade < 20:
        mulheres_menos_vinte +=1
    res = " "
    while res not in "SN":
        res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if res == "N":
        break
print(f'''Foram Cadastrados:
      {maior_idade} pessoas maiores de idade.
      {total_homens} homens cadastrados.
      {mulheres_menos_vinte} mulheres com menos de 20 anos.''')
