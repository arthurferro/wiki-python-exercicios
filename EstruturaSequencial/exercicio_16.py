'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
print("=" * len("===== Lata de Tinta 18 Litros: R$80,00 ====="))
print("===== Lata de Tinta 18 Litros: R$80,00 =====")
print("=" * len("===== Lata de Tinta 18 Litros: R$80,00 ====="))
print()
precoLata = 80
litrolata = 18
areaPintada = float(input("Digite a àrea a ser pintada: "))
litroUsado = areaPintada / 3
totalLatas = int(litroUsado / litrolata)
if litroUsado % litrolata != 0:
    totalLatas += 1
print("Quantidade de latas de tinta: %i" % (totalLatas))
print("Valor total lata de tintas: R$%.2f" % (totalLatas*80))
