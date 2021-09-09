'''Um professor quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada'''
#shuffle é para embaralhar.
from random import shuffle
aluno1 = str(input("Nome do aluno: "))
aluno2 = str(input("Nome do aluno2: "))
aluno3 = str(input("nome do aluno3: "))
aluno4 = str(input("Nome do aluno4: "))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print("a ordem de apresentação sera:  {}".format(lista))