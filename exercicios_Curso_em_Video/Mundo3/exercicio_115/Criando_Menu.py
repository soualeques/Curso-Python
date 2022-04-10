'''Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto 
simples. O sistema so vai ter 2 opçoes: cadastrar uma nova pessoa a listar todas as pessoas cadastradas'''
from menu import escolhas
from arquivo import *

if not arquivoExiste('Cursoemvideo.txt'):
    print('Arquivo nao existe... criando')
    criarArquivo('Cursoemvideo.txt')
else:
    print('Arquivo ja existe.')


escolhas('Sua escolha: ')
