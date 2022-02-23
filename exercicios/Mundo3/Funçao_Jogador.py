'''Faça um programa que tenha uma funçao chamada ficha(), que receba dois parametrosv opcionais:
o nome de um jogador e quantos gols ele marcou. O programa devera ser capaz de mostrar a ficha 
do jogador, mesmo que algum dado nao tenha sido informado corretamente'''

def ficha(nome= '<Desconhecido>', gols=0):
    if nome == "":
        nome = "<Desconhecido>"
    if gols == "":
        gols = 0
        
    return print(f'O jogador {nome} fez {gols} gols no campeonato!')


nome = str(input('Nome do jogador: ')).strip().title()
gols = str(input('Quantos gols ele marcou no campeonato? '))
ficha(nome, gols)
