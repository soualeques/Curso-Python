'''Faça um programa que tenha uma funçao notas() que pode receber varias notas de alunos e vai
retornar um dicionario com as seguintes informaçoes:
- Quantidades de notas
- A maior nota
- A media da turma
- A situaçao(opcional)
adicionar tambem docstrings.'''
from sqlalchemy import true


def notas(* n, sit=False):
    """
    ->Funcao que recebe varias notas de um aluno e mostra a maior nota, a media e 
    situaçao(opicional)
        n = notas do aluno;
        sit (bool, optional): mostrar ou nao a situaçao do aluno segundo suas notas.
    """
    aluno = {}
    media = 0
    maior = 0
    aluno["Total_Notas"] = len(n)
    aluno["Notas"] = n
    for v in aluno["Notas"]:
        if v == 0:
            maior = v
        else:
            if v > maior:
                maior = v
    aluno["Maior_Nota"] = maior
    media = sum(n) / len(n)
    aluno["Média"] = media
    aluno["Menor_Nota"] = min(n)
    if sit == True:
        if media <= 5:
            situaçao = "Ruim"
        elif media > 5 and media < 8:
            situaçao = "Razoavel"
        else:
            situaçao = "Boa"
        aluno["situaçao"] = situaçao
            
    return print(aluno)


#programa principal

notas(3,5,6,10, sit=True)