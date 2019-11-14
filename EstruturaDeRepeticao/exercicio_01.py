'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
from time import sleep
import os

os.system("cls")

i = True
while i == True:
    nota = float(input('Digite uma nota: '))
    if nota < 0 or nota > 10:
        print('Nota inválida. Digite uma nota entre 0 e 10')
        sleep(2.2)
        os.system("cls")
        i = True
    else:
        print(f'Nota {nota} é válida.')
        i = False
        sleep(3)
        os.system("cls")
