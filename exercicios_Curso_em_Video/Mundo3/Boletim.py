'''Crie um programa que leia o nome e notas de varios alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a media de cada aluno e permita ao usuario consultar a nota de 
cada aluno individualmente.'''
alunos = []

res = ''
while res != "N":
    nome = str(input('Nome do aluno: ')).strip()
    nota1 = float(input('1º nota: '))
    nota2 = float(input('2º nota: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1,nota2], media])
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('-=' * 30)
print(f'{"BOLETIM ESCOLAR":^30}')
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-=' * 30)
while True: 
    num = int(input('Quer ver a nota de qual aluno? [999 p/ parar] '))
    if num == 999:
         print('Finalizando programa...')
         break
    if num <= len(alunos) - 1:
        print(f'Notas de {alunos[num][0]} são: {alunos[num][1]}.')
print('----VOLTE SEMPRE-----')  

    