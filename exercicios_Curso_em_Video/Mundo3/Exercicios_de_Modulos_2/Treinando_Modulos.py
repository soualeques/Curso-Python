'''Adapte o codigo do treinado modulos, criando uma funçao chamada moeda() que consiga mostrar
os numeros como um valor monetario'''
import moedas
numero = float(input('Digite um valor: R$'))
print('-=' * 30)
print(f'A metade de {moedas.moeda(numero)} é: {moedas.moeda(moedas.metade(numero))}.')
print(f'O dobro de {moedas.moeda(numero)} é: {moedas.moeda(moedas.dobro(numero))}.')
print(f'Aumentando 10% de {moedas.moeda(numero)} fica: {moedas.moeda(moedas.aumentar(numero, 10))}.')
print(f'Diminuindo 18% de {moedas.moeda(numero)} fica: {moedas.moeda(moedas.diminuir(numero, 13))}.')
print('-=' * 30)