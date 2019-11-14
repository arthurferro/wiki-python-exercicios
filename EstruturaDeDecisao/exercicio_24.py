'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
'''


def operacao():
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    operador = int(
        input('Qual operação deseja efetuar? 1-(+), 2-(-), 3-(x), 4-(/): '))

    if operador == 1:
        operando = n1 + n2
        tipo_operacao = 'SOMA'
    elif operador == 2:
        operando = n1 - n2
        tipo_operacao = 'SUBTRAÇÃO'
    elif operador == 3:
        operando = n1 * n2
        tipo_operacao = 'MULTIPLICAÇÃO'
    elif operador == 4:
        operando = n1 / n2
        tipo_operacao = 'DIVISÃO'
    else:
        print('Operação inválida. Vamos iniciar novamente.')
        operacao()

    if (operando % 2) != 0:
        par_impar = 'ímpar'
    else:
        par_impar = 'par'

    if operando < 0:
        neg_pos = 'negativo'
    else:
        neg_pos = 'positivo'

    if operando == round(operando):
        dec_int = 'inteiro'
    else:
        dec_int = 'decimal'

    print(
        f'O resultado da operação de {tipo_operacao} entre {n1} e {n2} resultou em {operando}, o qual é um valor {par_impar},{neg_pos} e { dec_int}')


operacao()
