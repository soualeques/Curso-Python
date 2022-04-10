sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('ERRO! digite o Sexo corretamente [M/F]: ')).strip().upper()[0]
prioridade = str(input('Nível prioridade [ADM/USR/GUEST]: ')).upper().strip()

    
if sexo == "M" and prioridade == 'ADM':
    print('Olá Administrador')
elif sexo == "F" and prioridade == "ADM":
    print('Olá Administradora')
elif sexo == 'M' and prioridade == 'USR':
    print('Olá usúario')
elif sexo == 'F' and prioridade == "USR":
    print('Olá usúaria')
elif prioridade == 'GUEST':
    print('Ola visitante')
else:
    print('Olá Desconhecido(a)')
