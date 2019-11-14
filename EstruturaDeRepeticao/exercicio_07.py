'''
Faça um programa que leia 5 números e informe o maior número.
'''
maior = 0
for numero in range(1, 5 + 1):
    valor = float(input(f'Digite o {numero}. valor: '))
    if valor > maior:
        maior = valor
print(f'O maior número foi o {int(maior)}.')
