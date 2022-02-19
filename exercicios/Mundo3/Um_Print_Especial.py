'''Faça um programa que tenha uma função chamada escreva(). Que receba um texto qualquer
como parametro e mostre uma mensagem com tamanho adaptavel.'''
def escreva(txt):
    print('-' * len(txt))
    print(txt)
    print('-' * len(txt))
    
    
escreva('Olá Mundo!')
escreva('Esse é um programa feito por Alex Nascimento!')
escreva('Finalizando programa...')