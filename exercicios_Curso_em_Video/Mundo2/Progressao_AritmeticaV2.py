'''Refazer exercicio 'Progessao_Aritmetica' lendo o primeiro termo e a razao de uma PA.
mostrando os 10 primeiros termos da progressao usando a estrutura WHILE.'''

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont_termo = termo
cont = 1

while cont <= 10:
    print(f'{termo} -> ', end="")
    termo = termo + razao
    cont = cont + 1
print("Fim")