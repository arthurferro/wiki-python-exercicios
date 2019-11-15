##Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.##
lista = []

for i in range(1,6):
    valor = int(input(f"Digite o {i}º valor: "))
    lista.append(valor)


print(lista)