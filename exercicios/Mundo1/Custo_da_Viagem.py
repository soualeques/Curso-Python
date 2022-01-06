'''Desenvolva um programa que pergunte a distância de uma viagem
em Km. Calcule o preço da passagem. Cobrando R$0,50 por Km para viagens de até 200Km e 
R$0,45 para viagens mais longas'''

distancia = float(input("Digite a distancia da viagem em quilometros: "))
valorpassagem = distancia * 0.5
valorpassagemmaior = distancia * 0.45
if distancia <= 200:
    print(f"O valor da sua passagem será de R${valorpassagem:,.2f}")
else:
    print(f"O valor da sua passagem tera desconto e será de R${valorpassagemmaior:,.2f}")