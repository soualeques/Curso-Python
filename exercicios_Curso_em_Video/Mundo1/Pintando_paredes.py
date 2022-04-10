#Faça um programa que leia a altura e largura de uma parede e pinte ela, sabendo que cada litro pinta 2M²#
alt = float(input("Digite a altura em metros da parede a ser pintada: "))
larg = float(input("Digite a largura em metros da parede a ser pintada: "))
área = larg * alt
tinta = área / 2
print("sera necesario {}L de tinta para pintar a parede".format(tinta))