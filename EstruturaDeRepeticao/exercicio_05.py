'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''

paisA = int(input('Digite a população do país A: '))
paisB = int(input('Digite a população do país B: '))
taxaA = float(
    input('Digite a taxa de crescimento anual em porcentagem do país A: '))
taxaB = float(
    input('Digite a taxa de crescimento anual em porcentagem do país B: '))
anos = 0
while paisA < paisB:
    paisA += paisA * (taxaA / 100)
    paisB += paisB * (taxaB / 100)
    anos += 1

print('A ultrapassa ou iguala a B em %d anos' % anos)
