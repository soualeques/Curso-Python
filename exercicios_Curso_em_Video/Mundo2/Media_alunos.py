'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- média abaixo de 5.0: REPROVADO
- média entre 5.0 e 6.9: RECUPERAÇÃO
- média 7.0 ou suerior: APROVADO'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5.0:
    print(f'Sua média foi {media} e voce foi \033[1;31mREPROVADO!!!\033[m')
elif media == 5 and media < 6.9:
    print(f'Sua média foi de {media} e voce esta de \033[1;33mRECUPERAÇÃO!!!\033[m')
elif media >= 7.0:
    print(f'Sua média foi de {media} e voce foi \033[1;32mAPROVADO!!!\033[m')