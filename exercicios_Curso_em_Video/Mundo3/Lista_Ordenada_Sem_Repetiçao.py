'''Crie um programa que leia 5 valores e cadastre-os em uma lista ja na posição correta
de inserçao(sem usar o sort()). No final mostre a lista ordenada na tela.'''

numeros = []
for c in range(0,5):
    n = int(input('digite um valor: '))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram: {numeros}')
    