#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.#
#(0 °C × 9/5) + 32 = 32 °F#
grausC = float(input("Digite a temperatura em graus Celsius ºC: "))
print("A temperatura %.1fºC em graus Farenheit equivale a %.1fºF" %(grausC, (grausC*9)/5+32))