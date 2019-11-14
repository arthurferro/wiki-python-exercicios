'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
media_max = 10
nota_max = 10


def calcularMedia():
    n1 = float(input('Digite a sua primeira nota: '))
    n2 = float(input('Digite a sua segunda nota: '))
    n3 = float(input('Digite a sua terceira nota: '))
    media = (n1 + n2 + n3) / 3
    if n1 > nota_max or n2 > nota_max or n3 > nota_max:
        print('As notas não devem ser maiores que 10. Por favor, digite novamente.')
        calcularMedia()
    else:
        if media == 10:
            print('Aprovado com Distinção. Média: %.1f' % media)
        elif media >= 7:
            print('Aprovado. Media: %.1f' % media)
        elif media < 7:
            print('Reprovado. Média: %.1f' % media)


calcularMedia()
