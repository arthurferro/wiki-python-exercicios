'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''


def validarData():
    data = input('Digite uma data no formato dd/mm/aaaa: ')
    if len(data) == 10:
        if data[2] == '/' and data[5] == '/':
            dataFatiada = data.split('/')
            if int(dataFatiada[0]) > 0 and int(dataFatiada[0]) <= 31:
                if int(dataFatiada[1]) > 0 and int(dataFatiada[1]) <= 12:
                    if len(dataFatiada[2]) == 4 and int(dataFatiada[2]) != 0000:
                        print(f'Data Validada! -> {data}')
                    else:
                        print('Formato de ano errado')
                        validarData()
                else:
                    print('Formato de mês inválido. Por favor digite um mês de 1 a 12.')
                    validarData()
            else:
                print('Formato de dia inválido. Por favor digite um dia de 1 a 31.')
                validarData()
        else:
            print('Formato de data errada. Por favor digite no formato dd/mm/aaaa')
            validarData()
    else:
        print('Quantidade de caracteres errado. Por favor digite no formato dd/mm/aaaa')
        validarData()


validarData()
