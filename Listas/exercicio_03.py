##Faça um Programa que leia 4 notas, mostre as notas e a média na tela.##
notas = []
nota = 0
qtde_notas = int(input("Digite a quantidade de notas que será calculado a média: "))
qtde_notas+=1
print()
for i in range(1,qtde_notas):
    nota = float(input(f"Digite a {i}º nota: "))
    notas.append(nota)

print("%.1f" %(sum(notas) / len(notas)))