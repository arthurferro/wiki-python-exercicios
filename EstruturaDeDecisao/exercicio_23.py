'''
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
'''
n = float(input('Digite um número: '))

# Função round(n) arredonda o número sempre para o número par mais próximo.
if n == round(n):
    print('Inteiro')
else:
    print('Decimal')
    print('Arredondando para baixo: ', round(n-0.5))
    print('Arredondando para cima: ', round(n+0.5))
