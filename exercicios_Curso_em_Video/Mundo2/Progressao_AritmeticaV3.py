'''Melhore o exercicio 'Progressao_AritmeticaV2' perguntando ao usuario se ele quer
mostrar mais alguns termos. O programa encerra quando ele disse que quer mostrar 0 termos.'''

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
cont = 1
termo = primeiro_termo
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} -> ", end="")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos a mais quer mostrar?[DIGITE 0 PARA ENCERRAR] "))
print(f"Progressão Aritmetica finalizada com {total} termos mostrados!")
print("-----FIM DO PROGRAMA----")