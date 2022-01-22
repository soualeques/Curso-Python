'''Faça um programa que mostre a tabuada de varios numeros, um de cada vez
para cada valor digitado pelo usuario. O programa sera interrompido quando
o numero solicitado for negativo.'''

while True:
    numero = int(input('Quer ver a tabuada de qual numero? '))
    print('#'* 20)
    for c in range(0, 11):
        print(f'{numero} x {c} = {numero * c}')
    print('#'* 20)
    if numero < 0:
        break
print("----PROGRAMA FINALIZADO----")