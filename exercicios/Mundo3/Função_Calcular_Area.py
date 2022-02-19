'''Faça um programa que tenha uma função chamada área(). Que receba as dimensões de um terreno
retangular(largura e comprimento) e mostre a área do terreno.'''
def área(compr, larg):
    área = compr * larg
    print(f'A area do comprimento {compr:,.2f}m e largura {larg:,.2f}m é {área:,.2f}m².')


def titulo(txt):
    print('-' * 30)
    print(f'{txt:^20}')
    print('-' * 30)
    

#PROGRAMA PRINCIPAL    
titulo('CALCULO DE ÁREA')
comprimento = float(input('Digite o comprimento (m): '))
largura = float(input('Digite a largura (m): '))
área(comprimento, largura)
