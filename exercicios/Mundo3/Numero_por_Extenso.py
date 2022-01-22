'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso
de 0 a vinte. Seu programa devera ler pelo teclado(entre 0 e 20), e mostra-lo por extenso'''
''


numero_extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
,'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

numero = int(input("Digite um numero: "))
while numero not in range(0,21):
    numero = int(input("tente novamente...Digite um numero: "))
print(f'Voce digitou o numero {numero_extenso[numero]}.')
