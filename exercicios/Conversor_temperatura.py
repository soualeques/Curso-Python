#Faça um programa que converta uma temperatura digitada em ºC e converta para ºF#
C = float(input("Informe a temperatura em ºC: "))
f = ((9 * C)/5) + 32
print("A temperatura de {}ºC sera de {}ºF".format(C,f))