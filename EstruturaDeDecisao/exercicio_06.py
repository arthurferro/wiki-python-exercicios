#Faça um Programa que leia três números e mostre o maior deles.#
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
if n1 > n2 and n1 > n3:
    print(f'{n1} é maior.')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é maior')
elif n3 > n1 and n3 > n2:
    print(f'{n3} é maior')