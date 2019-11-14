'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

    DELTA = B² - 4.A.C
'''
from math import sqrt

print('-' * 15 + 'Calculadora de Raízes de uma Equação de Segundo Grau (Ax² + Bx + c)' + '-' * 15)
print()
a = float(input('Digite o valor de A: '))
if a == 0:
    print('A equação não é do segundo grau')
else:
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))
    delta = b**2 - (4 * a * c)
    if delta < 0:
        print('A equação não possui raízes reais.')
    elif delta == 0:
        print('A equação possui apenas uma raiz real.')
        x = (-4 + sqrt(delta)) / 2 * a
        print(f'Valor da raíz: {x}')
    elif delta > 0:
        print(f'A equação {a}x²+{b}x+{c} possui duas raízes reais.')
        x = (-4 + sqrt(delta)) / 2 * a
        print(f'Valor das raízes: {x} e {-x}')
