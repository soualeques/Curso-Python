'''Funçoes para importar no exercicio Testando_Modulos.py'''
def aumentar(num, taxa):
    aumento = num + (num * taxa / 100)
    return aumento


def diminuir(num, taxa):
    diminuiçao = num - (num * taxa / 100)
    return diminuiçao


def metade(num):
    met = num / 2
    return met


def dobro(num):
    dob = num * 2
    return dob    


def moeda(num=0, moeda ="R$"):
    return f"{moeda}{num:>4.2f}".replace('.', ',')
    
    