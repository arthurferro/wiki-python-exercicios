'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''
altura = float(input("Digite sua altura em metros: "))
print("Seu peso ideal masculino é %.2fkg." %((72.7*altura)-59))
print("Seu peso ideal feminino é %.2fkg." %((62.1*altura)-44.7))