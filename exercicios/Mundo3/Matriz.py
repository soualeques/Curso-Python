'''Crie um programa que crie uma matriz de dimensao 3x3 e preencha com os valores lidos pelo teclado
No final mostre a matriz com a formataçao correta.'''
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end="")
    print()    
    