'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                        Até 5 Kg            Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''
titulo = 'O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:'
print(titulo)
print('                               Até 5 Kg           Acima de 5 Kg')
print('COD=1    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg')
print('COD=2    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg')
print('COD=3    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg')
print('-' * len(titulo))
print()
print()
tipo = int(input('Digite o tipo da carne que você vai levar: '))
qtde_kg = float(input('Digite a quantidade em KGs: '))

if tipo == 1:
    if qtde_kg <= 5:
        precokg = 4.90
    else:
        precokg = 5.80
elif tipo == 2:
    if qtde_kg <= 5:
        precokg = 5.90
    else:
        precokg = 6.80
elif tipo == 3:
    if qtde_kg <= 5:
        precokg = 6.90
    else:
        precokg = 7.80

valor_total = qtde_kg * precokg

forma_pagamento = int(input('Vai pagar com o cartão Tabajara? 1-SIM 2-NÃO: '))
if forma_pagamento == 1:
    valor_total = valor_total - (valor_total * 5 / 100)
else:
    pass

print('Você vai pagar R${:.2f}'.format(valor_total))
