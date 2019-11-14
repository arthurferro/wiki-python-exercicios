'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''
n = int(input('Digite um número para saber se é ou não um número primo: '))
divisores = []

for divisor in range(1, n+1):
    if (n % divisor) == 0:
        divisores.append(divisor)
        if len(divisores) > 2:
            break

if len(divisores) > 2:
    print(f'{n} não é primo')
else:
    print(f'{n} é primo.')
