"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

n1 = float(input('Digite sua primeira nota de 0 a 10: '))
n2 = float(input('Digite sua segunda nota de 0 a 10:'))
media = (n1 + n2) / 2
conceito = ''
t_f = bool
a_r = ''
if media >= 9 and media <= 10:
    conceito = 'A'
    t_f = True
elif media < 9 and media >= 7.5:
    conceito = 'B'
    t_f = True
elif media < 7.5 and media >= 6:
    conceito = 'C'
    t_f = True
elif media < 6 and media >= 4:
    conceito = 'D'
    t_f = False
elif media < 4 and media >= 0:
    conceito = 'E'
    t_f = False


if t_f == True:
    a_r = 'Aprovado'
else:
    a_r = 'Reprovado'

print(
    f'Suas notas foram {n1} e {n2}\nSua média foi de {media}\nSeu conceito é {conceito} e você foi {a_r}')
