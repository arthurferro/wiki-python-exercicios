'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário
de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de
pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa
que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na 
variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João
deverá pagar. Imprima os dados do programa com as mensagens adequadas.'''

quilos = float(input("Digite quantos KG de peixe João pescou: "))
if quilos > 50:
    excesso = (50 - quilos) * -1
    multa = excesso * 4
    print("João ultrapassou os 50KG de peixes, excedendo %.1fKG e com uma multa de R$%.1f" %(excesso, multa))
    print("Multa de R$4.00 por KG.")
else:
    print("João pescou %.1fKG e não ultrapassou o limite de 50KG." %(quilos))