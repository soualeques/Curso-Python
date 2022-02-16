'''Aprimore o exercicio Matriz, mostrando agora:
- A soma dos valores pares;
- A soma dos valores da terceira coluna;
- O maior valor da segunda linha.'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_pares = soma_coluna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {[l],[c]}: '))
        
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end="")
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é: \033[1;32m{soma_pares}\033[m.')
for l in range(0, 3):
    soma_coluna += matriz[l][2]
print(f'A soma da terceira coluna é: \033[1;31m{soma_coluna}\033[m.')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha foi: \033[1;35m{maior}\033[m') 

