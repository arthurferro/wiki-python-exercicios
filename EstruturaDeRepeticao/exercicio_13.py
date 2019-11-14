'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
'''
base = int(input('Informe a base: '))
valor_base = base
expoente = int(input('\nInforme o expoente: '))

if (expoente == 1) or (expoente == 0):
    if (expoente == 1):
        print('\nResultado: %s' % (base))
    else:
        print('\nResultado: 1')
else:
    for i in (range(expoente-1)):
        base *= valor_base
    print('\nResultado: %s' % (base))
