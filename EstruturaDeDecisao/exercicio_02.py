#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.#
n = int(input("Digite um número: "))
if (n < 0):
    print('É negativo.')
elif (n > 0):
    print('É positivo.')
else:
    print('É nulo.')
