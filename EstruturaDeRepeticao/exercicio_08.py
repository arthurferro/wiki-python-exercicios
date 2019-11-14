'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
soma = 0
media = 0
contador = 0
for i in range(1, 5 + 1):
    numero = float(input(f'Digite o {i}. número: '))
    soma += numero
    media = soma / i

print(f'A soma dos números foi de {soma} e a média foi de {media}.')
