'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''
n = int(input('Digite um número para ser calculado seu fatorial: '))
resultado_fat = 1
for i in range(1, n+1):
    resultado_fat *= i

print(f'Resultado do fatorial de {n} é {resultado_fat}.')
