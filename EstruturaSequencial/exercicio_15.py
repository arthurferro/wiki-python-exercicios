'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
  o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
valorHora = float(input("Digite quanto você ganha por hora: "))
horaMes = float(input("Digite quantas horas no mês você trabalhou: "))
bruto = valorHora * horaMes
descontoIR = bruto * (11/100)
descontoINSS = bruto * (8/100)
descontoSindicato = bruto * (5/100)
liquido = bruto - descontoIR - descontoINSS - descontoSindicato
print(" + Salário Bruto:     R$%.2f" % (bruto))
print(" - Imposo de Renda:   R$%.2f" % (descontoIR))
print(" - Desconto INSS:     R$%.2f" % (descontoINSS))
print(" - Sindicato:         R$%.2f" % (descontoSindicato))
print(" = Salário Líquido:   R$%.2f" % (liquido))
