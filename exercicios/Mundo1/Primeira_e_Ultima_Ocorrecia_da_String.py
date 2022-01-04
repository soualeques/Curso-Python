'''Faça um programa que leia uma frase pelo teclado e mostre:
º  QUANTAS VEZES APARECE A LETRA "A";
º  EM QUE POSIÇÃO ELA APARECE PELA PRIMEIRA VEZ;
º  EM QUE POSIÇÃO ELA APARECE PELA ULTIMA VEZ.'''

frase = str(input("Digite uma frase: ")).strip().upper()

print(f"A letra 'A' aparece {frase.count('A')} vezes")
print(f"A primeira letra 'A' aparece na posição {frase.find('A', +1)}")
print(f"A ultima letra 'A' aparece na posição {frase.rfind('A', +1)}")