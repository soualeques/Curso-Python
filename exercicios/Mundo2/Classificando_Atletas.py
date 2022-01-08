'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento do atleta
e mostre sua categoria, de acordo com a idade:
- ate 9 anos: MIRIN
- ate 14 anos: INFANTIL
- ate 19 anos: JUNIOR
- ate 25 anos: SENIOR
- acima: MASTER
'''
from datetime import date

data_atual = date.today().year
ano_nascimento = int(input("Ano de nascimento: "))
idade = data_atual - ano_nascimento

print(f"O atleta cadastrado tem {idade} anos.")

if idade <= 9:
    print(f'E esta classificado na categoria: \033[1;32mMIRIN\033[m')
elif idade >9 and idade <= 14:
    print(f'E esta classificado na categoria: \033[1;32mINFANTIL\033[m')
elif idade >14 and idade <= 19:
    print(f'E esta classificado na categoria: \033[1;32mJUNIOR\033[m')
elif idade >19 and idade <= 25:
    print(f'E esta classificado na categoria: \033[1;32mSENIOR\033[m')
elif idade > 25:
    print(f'E esta classificado na categoria: \033[1;32mMASTER\033[m')