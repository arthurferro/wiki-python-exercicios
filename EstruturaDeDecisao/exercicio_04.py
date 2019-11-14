#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.#
vogais = 'aeiou'
consoantes = 'bcdfghjklmnpqrstvwxyz'
letra = input('Digite uma letra: ')
if (letra.lower() not in vogais):
    print('É uma consoante')
elif (letra.lower() not in consoantes):
    print('É uma vogal')