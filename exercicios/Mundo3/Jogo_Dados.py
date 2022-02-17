'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios.
Guarde esses resultados em um dicionario. No final, coloque esse dicionario em ordem,
sabendo que o vencedor tirou o maior numero no dado.'''

from operator import itemgetter
from random import randint
from time import sleep

jogadores = {
    'Jogador1': randint(1,6),
    'Jogador2': randint(1,6),
    'Jogadoe3': randint(1,6),
    'Jogador4': randint(1,6)
}
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado!')
    sleep(1)
ranking = []
print('-=' * 30)
print('=== RANKING ===')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'   {i+1}º LUGAR: {v[0]} com {v[1]}.')
    sleep(1)
    