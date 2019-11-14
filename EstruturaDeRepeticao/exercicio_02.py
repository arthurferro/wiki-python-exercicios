'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''
import os
from time import sleep
os.system('cls')
i = True
ret = ['.', '.', '.']
while i == True:
    usuario = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')
    if senha == usuario:
        print('Sua senha não pode ser igual ao seu nome de usuário...')
        sleep(2)
        os.system('cls')
        print('Vamos recomeçar...')
        sleep(1)
        i = True
        os.system('cls')
    else:
        os.system('cls')
        print('Conta criada com sucesso!')
        sleep(5)
        os.system('cls')
        i = False   