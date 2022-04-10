''''Escreva um programa que leia a velocidade de um carro, se ele 
ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input("Digite a velocidade do carro em quilometros: "))
multaparapagar = velocidade - 80
multa = multaparapagar * 7
if velocidade <= 80:
    print("Velocidade permitida, continue dirigindo com segurança!")
else:
    print(f"Você ultrapassou o limite de velocidade e foi multado em R${multa:,.2f}")