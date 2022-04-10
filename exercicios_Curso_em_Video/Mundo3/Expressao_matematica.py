'''Crie um programa onde o usuario digite uma expressao matematica usando parenteses
e seu programa devera identificar se a expressao esta com os parenteses abrindo e fechando
na ordem correta.'''

pilha = []
expressao = str(input('Digite uma expressao matematica: '))
for simb in expressao:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print('Sua expressao esta valida!')
else:
    print('Sua expressao esta invalida!')