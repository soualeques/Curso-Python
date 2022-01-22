'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol
, na ordem de colocação. Depois mostre:
- Apenas os 5 primeiros colocados;
- Os ultimos 4 colocados da tabela;
- Uma lista com os times em ordem alfabetica;
- Em que posiçao da tabela esta o Corinthians.'''
#Exercicio feito 21/01/2022

brasileirao = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
'Corinthians', 'Bragantino', 'Fluminense', 'América-MG','Atlético-GO','Santos','Ceará','Internacional'
,'São Paulo','Athletico-PR','Cuiabá','Juventude','Grêmio','Bahia','Sport','Chapecoense')

print('*-'*20)
print('{:^40}'.format('BRASILEIRAO'))
print('*-'*20)

print(f"OS 5 PRIMEIROS COLOCADOS SÃO: \033[1;32m{brasileirao[:5]}\033[m")
print('*-'*20)
print(f'OS ULTIMOS 4 COLOCADOS SÃO: \033[1;31m{brasileirao[-4:]}\033[m')
print('*-'*20)
print(f'TABELA EM ORDEM ALFABETICA: \033[1;33m{sorted(brasileirao)}\033[m')
print('*-'*20)
print(f'O CORINTHIANS SE ENCONTRA NA POSIÇÃO \033[1;34m{brasileirao.index("Corinthians") + 1}\033[m')
print('*-'*20)
