'''Modifique as funçoes que foram criadas no treinamento_modulos.py para que elas aceitem um parametro
a mais, informando se o valor retornado por elas vai ou nao formatado pela funçao moeda().'''
import moedas
numero = float(input('Digite um valor: R$'))
print('-=' * 30)
print(f'A metade de {moedas.moeda(numero)} é: {(moedas.metade(numero, format=True))}.')
print(f'O dobro de {moedas.moeda(numero)} é: {moedas.dobro(numero, format=True)}.')
print(f'Aumentando 10% de {moedas.moeda(numero)} fica: {moedas.aumentar(numero, 10, format=True)}.')
print(f'Diminuindo 15% de {moedas.moeda(numero)} fica: {moedas.diminuir(numero, 15, format=True)}.')
print('-=' * 30)