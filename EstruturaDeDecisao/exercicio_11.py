'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o         programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;   o valor do aumento;
o novo salário, após o aumento.
'''
salario_base = float(input("Digite o salário de um colaborador: "))

if salario_base > 0 and salario_base <= 280:
    valor_aumento = salario_base * 0.20
    valor_percentual = '20%'
elif salario_base > 280 and salario_base <= 700:
    valor_aumento = salario_base * 0.15
    valor_percentual = '15%'
elif salario_base > 700 and salario_base <= 1500:
    valor_aumento = salario_base * 0.10
    valor_percentual = '10%'
elif salario_base > 1500:
    valor_aumento = salario_base * 0.05
    valor_percentual = '05%'

salario_novo = salario_base + valor_aumento

print('Salário antes do reajuste  >  R$%.2f' %(salario_base))
print(f'Percentual aplicado  >  {valor_percentual}')
print('Valor do reajuste  >  R$%.2f' %(valor_aumento))
print('Salário após reajuste  >  %.2f' %(salario_novo))