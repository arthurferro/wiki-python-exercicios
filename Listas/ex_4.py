##Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.##
vetor = []
vogais = ['a','e','i','o','u']
consoantes = []
for i in range(1,11):
    letra = input("Digite uma letra: ")
    letra = letra.lower
    if letra in vogais:
        vetor.append(letra)
    else:
        vetor.append(letra)
        consoantes.append(letra)

print(f"Todas as letras digitadas: {vetor}")
print(f"Quantidade de consoantes: {sum(consoantes)}")
print(f"Todas as consoantes: {consoantes}")
