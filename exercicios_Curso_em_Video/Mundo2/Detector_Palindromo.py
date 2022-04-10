'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando
os espaços (ou seja, pode ser lida de tras pra frente e da frente pra traz)'''

frase = str(input("Digite uma frase: ")).strip().upper()
separado = frase.strip()
junto = "".join(separado)
inverso = ""
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}.")
if inverso == junto:
    print("Temos um palindromo!")
else:
    print('a frase digitada nao é um palindromo!')

