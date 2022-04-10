'''Crie um programa que leia o nome de uma pessoa e 
diga se tem "Silva" no nome'''

nome = str(input("Qual o seu nome? ")).strip()
print("tem silva no seu nome? ")
print("SILVA" in nome.upper())
