'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''
qtde_morango = float(input('Digite quantos KGs de morango você quer: '))
qtde_maca = float(input('Digite quantos KGs de maçã você quer: '))
total_kg = qtde_maca + qtde_morango

if qtde_morango <= 5:
    valor_morango_kg = 2.50
else:
    valor_morango_kg = 2.20
if qtde_maca <= 5:
    valor_maca_kg = 1.80
else:
    valor_maca_kg = 1.50

valor_compra = (qtde_morango * valor_morango_kg) + (qtde_maca * valor_maca_kg)
valor_sem_desconto = valor_compra
if total_kg > 8 or valor_compra > 25:
    valor_compra = valor_compra - (valor_compra * 10 / 100)

print('Você pagaria um total de R${:.2f}'.format(valor_sem_desconto))
print('Você pagará um total de R${:.2f} com 10% de desconto.'.format(
    valor_compra))
