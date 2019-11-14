'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''
condicao = True
numeros = []

while condicao:
    n = int(input('Digite um número: '))
    if n != 0:
        numeros.append(n)
    else:
        break

print(f'A soma dos número resulta em: {sum(numeros)}.')
print(f'o maior número é: {max(numeros)}.')
print(f'O menor número é: {min(numeros)}.')