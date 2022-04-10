'''Crie um pacote chamado utilidadesCeV que tenha dois modulos internos chamados moeda e dado.
transfira todas as funçoes utilizadas nos desafios anteriores e mantenha tudo funcionando.'''
from utilidadesCeV import moeda
from utilidadesCeV import dados
numero = dados.leiaDinheiro('Digite um valor: R$')
mais = int(input('Taxa de aumento: '))
menos = int(input('Taxa de desconto: '))
moeda.resumo(numero, mais, menos)