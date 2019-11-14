'''
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
'''
numeros = 20

for numero in range(1, numeros + 1):
    if numero == 20:
        print(numero, end='.')
    else:
        print(numero, end=', ')
