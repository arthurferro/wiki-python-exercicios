#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
## imprima o número de alunos com média maior ou igual a 7.0.#
import os
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')
mediaNotasAlunos = []
mediaAluno = []
qtdMediaMaior = float(input("Digite a média suficiente de cada aluno: "))
nAlunosMedia = 0
print("Vamos começar...")
sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

for a in range (1,3):
    for n in range(1,5):
        nota = float(input(f"Digite a {n}º nota do {a}º aluno: "))
        mediaAluno.append(nota)
    print("Aguarde...")
    sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    mediaNotasAlunos.append(sum(mediaAluno)/len(mediaAluno))
    

for media in mediaNotasAlunos:
    if media >= qtdMediaMaior:
        nAlunosMedia+=1

print(f"Número de alunos com média maior que {qtdMediaMaior}: {nAlunosMedia} aluno(s)")

print('test')