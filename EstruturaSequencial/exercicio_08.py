#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.#
valorHora = float(input("Digite quanto você ganha por hora: R$"))
horasMes = float(input("Horas trabalhadas no mês: "))
print("Salário: R$%.2f" %(valorHora*horasMes))