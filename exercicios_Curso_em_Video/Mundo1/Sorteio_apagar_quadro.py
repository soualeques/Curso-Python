'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um 
programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido'''
from random import choice
aluno1 = str(input("Nome do aluno: "))
aluno2 = str(input("Nome do aluno2: "))
aluno3 = str(input("nome do aluno3: "))
aluno4 = str(input("Nome do aluno4: "))
escolhido = choice([aluno1, aluno2, aluno3, aluno4])
print("O escolhido para apagar o quadro foi {}".format(escolhido))