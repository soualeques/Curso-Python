'''Crie um modulo chamado moedas.py que tenha funçoes incorporardas aumentar(), diminuir(), dobro() e 
metade(). Faça tambem um programa que importe esse modulo e importe algumas dessa funçoes.'''
import moedas
numero = float(input('Digite um valor: R$'))
print(f'A metade de R${numero} é: R${moedas.metade(numero)}.')
print(f'O dobro de R${numero} é: R${moedas.dobro(numero)}.')
print(f'Aumentando 10% de R${numero} fica: R${moedas.aumentar(numero, 10)}.')
print(f'Diminuindo 18% de R${numero} fica: R${moedas.diminuir(numero, 13)}.')