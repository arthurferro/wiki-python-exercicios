'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = float(input("Digite um terceiro número real: "))
print('1 - O produto do dobro do primeiro com metade do segundo:')
print("2 x %i + %i / 2 = %.1f" %(n1,n2, ((n1*2)+(n2/2))))
print()
print('2 - A soma do triplo do primeiro com o terceiro:')
print("3 x %i + %.2f = %.1f" %(n1, n3, float(n1*3+n3)))
print()
print('3 - O terceiro elevado ao cubo:')
print("%.2f³ = %.2f" %(n3, n3**3))