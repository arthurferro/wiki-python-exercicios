#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.#
lado = float(input("Digite o lado de um quadrado[metros]: "))
print("A área do quadrado equivale a %.2fm² e seu dobro equivale a %.2fm²" % (lado**2, (lado**2)*2))