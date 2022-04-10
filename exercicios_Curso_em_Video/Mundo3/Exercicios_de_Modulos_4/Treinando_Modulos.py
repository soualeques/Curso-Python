'''Adicione ao modulo moeda.py criado nos desafios anteriores, uma funçao chamada resumo(), que
mostre na tela algumas informaçoes pelas funçoes que ja temos no modulo criado ate aqui.'''
import moedas
numero = float(input('Digite um valor: R$'))
mais = int(input('Taxa de aumento: '))
menos = int(input('Taxa de desconto: '))
moedas.resumo(numero, mais, menos)