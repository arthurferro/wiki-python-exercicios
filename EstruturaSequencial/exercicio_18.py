##Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).##
arquivo = int(input("Digite o tamanho do arquivo em MB: "))
velocidade_internet = int(input("Digite a velocidade da sua internet em Mbs: "))
MBs = velocidade_internet * 0.125
duracao_download_segundos = arquivo / MBs
duracao_download_minutos = duracao_download_segundos / 60
print("Tempo aproximado de download: %.0f minutos" % (duracao_download_minutos))