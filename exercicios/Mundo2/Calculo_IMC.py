'''Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule o IMC e mostre seu status
de acordo com a tabela abaixo:
- Abaixo de 18.5: ABAIXO DO PESO
- Entre 18.5 e 25: PESO IDEAL
- 25 ate 30: SOBREPESO
- 30 ate 40: OBESIDADE
- Acima de 40: OBESIDADE MORBIDA'''

altura = float(input("Digite sua altura: (m)"))
peso = float(input("Digite seu peso atual: (Kg)"))
IMC = peso / (altura * altura)
print(f'De acordo com seus dados seu IMC é de {IMC:,.2f}')

if IMC < 18.5:
    print(f'Abaixo do peso')
elif IMC >= 18.5 and IMC < 25:
    print(f'\033[1;32mvoce esta no Peso Ideal\033[m')
elif IMC > 25 and IMC <= 30:
    print(f'Voce esta com Sobrepeso')
elif IMC > 30 and IMC <= 40:
    print(f'voce esta com Obesidade')
elif IMC > 40:
    print(f'\033[1;31voce esta com Obesidade Morbida, cuidado!\033[m')