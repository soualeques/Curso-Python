'''Crie um programa que leia varios numeros inteiros pelo teclado. No final da execuçao
, mostre a media entre todos os valores e qual foi o maior e menor valores lidos. o programa deve
perguntar ao usuario se ele quer ou nao digitar novos valores.'''

res = " "
quant_numeros = 0
maior = menor = 0 
soma = 0
while res not in "Nn":
    numero = int(input("Digite um valor: "))
    quant_numeros += 1
    res = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
    while res not in "SsNn":
        print("Resposta invalida")
        res = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
    soma += numero
    if quant_numeros == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
media = soma / quant_numeros
print(f'foi digitado {quant_numeros} numeros')
print(f'A media foi de {media}')
print(f"O maior numero digitado foi {maior} e o menor numero digitado foi {menor}.")    