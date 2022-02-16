'''Faça um programa que leia o nome e média de um aluno, guardando tambem a situação em um
dicionario. No final mostre o conteudo da estrutura na tela'''
boletim = {}
nome = str(input('Nome: ')).strip()
media = float(input(f'Media do {nome}: '))
if media > 7:
    situaçao = 'Aprovado'
else:
    situaçao = 'Reprovado'
boletim['nome'] =  nome
boletim['media'] = media
boletim['Situação'] = situaçao

for k, v in boletim.items():
    print(f'{k} é igual a {v}.')