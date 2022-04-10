'''Crie um programa onde o usuario pode digitar varios valores numericos e cadastre-os em uma lista
caso o numero ja esteja la dentro, nao sera adicionado. No final sera mostrado todos os numeros
digitados em ordem crescente'''
lista_numeros = []
while True:
    numero_novo = int(input('DIgite um valor: '))
    if numero_novo not in lista_numeros:
        lista_numeros.append(numero_novo)
        print('\033[1;32mNumero adicionado com sucesso!\033[m')
    else:
        print('\033[1;31mNumero duplicado!\033[m')
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while res not in "SN":
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if res == "N":
        break
print('-='*30)
print(f'Os numeros adicionados foram: \n{sorted(lista_numeros)}')
    
    