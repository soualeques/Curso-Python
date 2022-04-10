'''Desenvolva um proframa que leia o comprimento de tres retas e diga
ao usuario se elas podem ou nao forma um triangulo'''

print("_-_"*20)
print("analisador de trinagulos")
print("_-_"*20)

comprimento1 = float(input("Digite um comprimento: "))
comprimento2 = float(input("Digite outro comprimento: "))
comprimento3 = float(input("Digite mais um comprimento: "))

if comprimento1 < comprimento2 + comprimento3 and comprimento2 < comprimento1 + comprimento3 and comprimento3 < comprimento2 + comprimento1:
    print("\033[1;32mEsses segmentos formam um triangulo!\033[m")
else:
    print('\033[4;31mEsses segmentos nao formam um triangulo!\033[m')
