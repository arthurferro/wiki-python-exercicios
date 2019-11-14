##Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
##Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
vetor_completo = []
pares = []
impares = []

for i in range (1,5):
    numero = int(input(f"Digite o {i}º valor: "))
    vetor_completo.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Todos os valores: {vetor_completo}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")