#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].#
import os
numero = int(input("Digite um número: "))
os.system('cls' if os.name == 'nt' else 'clear')
print(f"O número informado foi: {numero}")