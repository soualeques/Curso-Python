medida = float(input("Uma distância em metros: "))
cm = medida * 100
mm = medida * 1000
print('A medida de {}M corresponde a {:.0f}CM e {:.0f}mm'.format(medida,cm,mm))