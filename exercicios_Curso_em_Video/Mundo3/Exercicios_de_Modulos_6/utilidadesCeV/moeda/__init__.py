'''Funçoes para importar no exercicio Testando_Modulos.py'''
def aumentar(num, taxa=0, format=False):
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


def diminuir(num, taxa=0, format=False):
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
    
    
def resumo(num=0, mais=0, menos=0):
    print('-' * 35)
    print(f'{"RESUMO":^30}')
    print('-' * 35)
    print(f'{"Preço analisado:"}\t{moeda(num)}')
    print(f'{"Dobro do preço:"} \t{dobro(num, True)}')
    print(f'{"Metade do preço:"}\t{metade(num, True)}')
    print(f'Aumento de {mais}%: \t{aumentar(num,mais, True)}')
    print(f'Diminuiçao de {menos}%:\t{diminuir(num,menos, True)}')
    print('-' * 35)