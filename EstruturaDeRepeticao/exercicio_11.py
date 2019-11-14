'''
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
Altere o programa anterior para mostrar no final a soma dos números.
'''
soma = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print(f'O(s) número(s) que está(ão) entre {n1} e {n2} é(são): ', end='')
for i in range(n1 + 1, n2):
    if i == (n2 - 1):
        print(i, end='.')
    elif i == (n2 - 2):
        print(i, end=' e ')
    else:
        print(i, end=', ')
    soma += i

print()
print(f'A soma dos números entre {n1} e {n2} resulta em {soma}.')
