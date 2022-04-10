'''Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla.
No final mostre:
- Quantas vezes aparece o valor 9
- Em que posição foi digitado o primeiro valor 3
- quantos foram os numeros pares'''



n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite outro valor: '))
n4 = int(input('Digite outro valor: '))
numeros = (n1, n2, n3, n4)
par = 0
print(f'O VALOR 9 FOI DIGITADO {numeros.count(9)} VEZES')
if 3 in numeros:
    print(f'O VALOR 3 FOI ENCONTRADO PELA PRIMEIRA VEZ NA POSIÇÃO {numeros.index(3)}')
else:
    print('O VALOR 3 NAO FOI DIGITADO.')
for c in numeros:
    if c % 2 == 0:
        print(f'{c}', end=" ")
        par +=1
print(f'FORAM OS NUMEROS DIGITADOS PARES, TOTAL DE {par} NUMEROS PARES.')