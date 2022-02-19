'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois 
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso sera guardado em
um dicionario, incluindo o total de gols feitos durante o campeonato.'''
jogador = {}
gols = []
total_gols = 0
jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou?  '))
for i, c in enumerate(range(0, partidas)):
    gol_partida = int(input(f'Quantos gols na partida {i+1}: '))
    gols.append(gol_partida)
    total_gols += gol_partida
    
jogador['Gols'] = gols
jogador['Total_gols'] = total_gols
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo \033[1;34m{k}\033[m tem o valor \033[1;34m{v}\033[m.')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for i, p in enumerate(jogador['Gols']):
    print(f'  -> Na partida \033[1;36m{i+1}\033[m ele fez \033[1;36m{p}\033[m gol(s)')
print(f'Foi um total de \033[1;36m{total_gols}\033[m gols.')