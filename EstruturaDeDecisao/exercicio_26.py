'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''
print('Gasolina R$2,50    |    Alcool R$1,90')
n_litros = float(input('Número de Litros: '))
resp = input('Gasolina(G) ou Alcool(A)    :')

if resp.upper() == 'A':
    resp = 'Alcool'
    preco = 1.90
    if n_litros <= 20:
        desconto = 3
    else:
        desconto = 5
if resp.upper() == 'G':
    resp = 'Gasolina'
    preco = 2.50
    if n_litros <= 20:
        desconto = 4
    else:
        desconto = 6

# calculo total com desconto
total_com_desconto = 1 * preco - (1 * preco * desconto / 100)

print(
    f'O valor a ser pago para {n_litros} litro(s) de {resp} é: R${round(total_com_desconto,2)}')
