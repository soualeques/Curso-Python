'''Elabore um programa que calcule o valor a ser pago por um produto, considerando seu
preço normal e condição de pagamento:
- á vista dinheiro/cheque: 10% de desconto
- á vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

print("-*-"*8)
print('\033[1;36;41m     LOJA DO ALEX     \033[m')
print("-*-"*8)
produto = float(input("Valor do produto: R$"))
desconto_a_vista = produto - (produto * 10 /100)
desconto_no_cartao = produto - (produto * 5 / 100)
parcela2x = produto / 2
juros_parcelado = produto + (produto * 20 / 100)

forma_pagamento = int(input('''Forma de pagamento:
                            [1] Á VISTA DINHEIRO/CHEQUE
                            [2] Á VISTA NO CARTÃO
                            [3] 2X NO CARTÃO
                            [4] 3X OU MAIS NO CARTÃO
                            sua escolha:'''))
if forma_pagamento == 1:
    print(f'Nessa forma de pagamento você obteve desconto de 10% e o valor de R${produto:,.2f} passara \na ser R${desconto_a_vista:,.2f}.')
elif forma_pagamento == 2:
    print(f'Nessa forma de pagamento você obteve desconto de 5% e o valor de R${produto:,.2f} passara \na ser R${desconto_no_cartao:,.2f}. ')
elif forma_pagamento == 3:
    print(f'Nessa forma de pagamento o produto de R${produto:,.2f} você terá 2 parcelas de R${parcela2x:,.2f}. ')
elif forma_pagamento == 4:
    parcelas = int(input('Parcelar em quantas vezes? '))
    parcelas3xmais = juros_parcelado / parcelas 
    print(f'Nessa forma de pagamento o produto obteve juros de 20% custando agora R${juros_parcelado:,.2f}, e foi parcelado em {parcelas} \ncustando cada parcela R${parcelas3xmais:,.2f}.')
print('\033[7;40m-------FIM DO PROGRAMA--------\033[m')