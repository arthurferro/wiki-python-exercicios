'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''
n_pares = 0
n_impares = 0

for i in range(1, 10 + 1):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        n_pares += 1
    else:
        n_impares += 1

print(f'Quantidade de números pares: {n_pares}')
print(f'Quantidade de números ímpares: {n_impares}')
