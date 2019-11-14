'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''


condicao = True
numeros = []
print('Ler números: Digite um número de 1 a 1000. Digite 0 para calcular os números.')
while condicao:
    n = int(input('Digite um número: '))
    if n > 0 and n < 1000:
        numeros.append(n)
    elif n == 0:
        break
    else:
        print('Valor inválido. Vamos iniciar novamente.')
        numeros = []
        condicao = True

print(f'A soma dos número resulta em: {sum(numeros)}.')
print(f'o maior número é: {max(numeros)}.')
print(f'O menor número é: {min(numeros)}.')
