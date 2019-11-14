'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
'''
import os

os.system('cls')
condicao = True
while condicao:
    n = int(input('Digite um número para ser calculado seu fatorial: '))
    if n > 0 and n <= 16:
        resultado_fat = 1
        for i in range(1, n+1):
            resultado_fat *= i
        print(f'Resultado do fatorial de {n} é {resultado_fat}.')
        r = int(input('Deseja calcular novamente? (1)-SIM (2)-NÃO: '))
        if r == 1:
            os.system('cls')
            condicao = True
        else:
            break
    else:
        print('Valor inválido. Vamos iniciar novamente...')
        condicao = True
