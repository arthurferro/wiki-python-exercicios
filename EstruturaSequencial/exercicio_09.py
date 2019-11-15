#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
#C = (5 * (F-32) / 9).#
grausF = float(input("Digite a temperatura em Farenheit: "))
print("A temperatura %.1fºF em graus Celsius equivale a %.1fºC" %(grausF, 5*(grausF-32)/9))