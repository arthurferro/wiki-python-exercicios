"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
from time import sleep
i = True
while i == True:
    n = int(input('Insira um número para exibir o dia correspondente da semana: '))
    if n == 1:
        print('Domingo')
        i = False
    elif n == 2:
        print('Segunda-Feira')
        i = False
    elif n == 3:
        print('Terça-Feira')
        i = False
    elif n == 4:
        print('Quarta-Feira')
        i = False
    elif n == 5:
        print('Quinta-Feira')
        i = False
    elif n == 6:
        print('Sexta-Feira')
        i = False
    elif n > 6:
        print('Valor Inválido')
        sleep(2)
        i = True
