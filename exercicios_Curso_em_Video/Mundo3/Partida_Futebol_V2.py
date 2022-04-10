'''Aprimore o exercicio Partida_Futebol.py para que ele funcione com varios jogadores, incluindo
um sistema de visualização de detalhes de aproveitamento de cada jogador'''
from pkg_resources import ensure_directory


jogador = {}
gols = []
jogadores = []
while True:   
    jogador.clear()
    gols.clear()
    total_gols = 0
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?  '))
    for i, c in enumerate(range(0, partidas)):
        gol_partida = int(input(f'Quantos gols na partida {i+1}: '))
        gols.append(gol_partida)
        total_gols += gol_partida
    jogador['Gols'] = gols[:]
    jogador['Total_gols'] = total_gols
    jogadores.append(jogador.copy())
    res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while res not in "SN":
        res = str(input('Digito errado! Digite apenas S ou N: '))
    if res == "N":
        break
print('-=' * 30)
print(jogadores)
print('-=' * 30)
print('Cod ', end="")
for i in jogador.keys():
    print(f'{i:<15}', end="")
print()
print('-'* 40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end="")
    for d in v.values():
        print(f'{str(d):<15}', end="")
    print()
print('-'* 40)
while True: 
    num = int(input('Quer ver o aproveitamento de qual jogador? \nDigite o Codigo de tal [999 p/ parar] : '))
    if num == 999:
         print('Finalizando programa...')
         break
    if num <= len(jogadores) - 1:
        print('-='*30)
        print(f'O jogador \033[1;32m{jogadores[num]["Nome"]}\033[m jogou {partidas} partidas.')
        for i, p in enumerate(jogadores[num]['Gols']):
            print(f'  -> Na partida \033[1;36m{i+1}\033[m ele fez \033[1;36m{p}\033[m gol(s)')
        print(f'Foi um total de \033[1;36m{total_gols}\033[m gols no campeonato.')
        print('-='*30)
    else:
        print(f"\033[1;31mCodigo {num} nao existe, por favor coloque outro!\033[m")
print('<< VOLTE SEMPRE \033[1;34m:)\033[m >>')