'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele AINDA VAI SE ALISTAR ao serviço militar, se é a HORA DE SE ALISTAR ou se JA PASSOU O TEMPO
do alistamento.
Seu programa tambem devera mostrar o tempo que falta ou que passou.'''

from datetime import date

print("-*-"*15)
print("\033[7;40m!!PROGRAMA DE ALISTAMENTO MILITAR!!\033[m")
print("-*-"*15)
sexo = str(input("Sexo: [M/F]")).strip().upper()
if sexo == "F":
    print("O alistamento nao é obrigatorio para o sexo feminino!")
ano_nascimento = int(input("Ano de nascimento: "))
idade = date.today().year - ano_nascimento

print(f"Nascido em {ano_nascimento} hoje voce tem {idade} anos!")
if idade < 18:
    maior_de_idade = 18 - idade
    ano_alistamento = maior_de_idade + date.today().year 
    print(f"Voce ainda vai se alistar!, faltam {maior_de_idade} anos.")
    print(f"Seu alistamento sera no ano {ano_alistamento}.")
elif idade == 18:
    print("Esta na hora de se alistar!")
elif idade > 18:
    passou_idade = idade - 18
    ano_alistamento = date.today().year - passou_idade 
    print(f"Ja passou o tempo para se alistar! Deveria ter se alistado ha {passou_idade} anos.")
    print(f"Seu alistamento deveria ser no ano {ano_alistamento}.")
