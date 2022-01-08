'''Refaça o desafio dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera
formado:
- EQUILATERO = todos os lados iguais
- ISOSCELES =  dois lados iguais
- ESCALENO =  todos os lados diferentes'''

segmento1 = float(input('Primeiro segmento: '))
segmento2 = float(input('Segundo segmento: '))
segmento3 = float(input('Terceiro segmento: '))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print('Esses segmentos formam um triangulo ')
    if segmento1 == segmento2 == segmento3:
        print('EQUILATERO!')
    elif segmento1 != segmento2 != segmento3 != segmento1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Esses segmentos nao formam um triangulo')

