##Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.##

lista = []

for i in range(1,11):
    valor = int(input(f"Digite o {i}º valor: "))
    lista.append(valor)

lista.reverse()
print(lista)