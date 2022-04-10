'''Refazer exercicio da tabuada com laço de repetição FOR'''

numero = int(input("Que numero quer ver a tabuada? "))

for c in range(0, 10 + 1 ):
    print(f'{numero} X {c} = {numero * c}')
print("----FIM DO PROGRAMA----")