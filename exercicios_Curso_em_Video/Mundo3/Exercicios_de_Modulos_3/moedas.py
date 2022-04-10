'''Funçoes para importar no exercicio Testando_Modulos.py'''
def aumentar(num, taxa, format=False):
    """Funcao para aumentar o valor digitado pelo usuario de acordo com a taxa.

    Args:
        num: valor digitado pelo usuario;
        taxa (_type_): taxa que vai aumentar o num;
        format (bool, optional):parametro para formatar ou nao o valor como dinheiro.

    Returns:
        valor digitado pelo usuario + a taxa
    """
    aumento = num + (num * taxa / 100)
    if format == True:
        return moeda(aumento)
    return aumento


def diminuir(num, taxa, format=False):
    diminuiçao = num - (num * taxa / 100)
    if format == True:
        return moeda(diminuiçao)
    return diminuiçao


def metade(num, format=False):
    met = num / 2
    if format == True:
        return moeda(met)
    return met


def dobro(num, format=False):
    dob = num * 2
    if format == True:
        return moeda(dob)
    return dob    


def moeda(num=0, moeda ="R$"):
    return f"{moeda}{num:>4.2f}".replace('.', ',')
    
    