import csv

# Nome do arquivo CSV
arquivo_csv = "pessoas.csv"

# Abrindo o arquivo e lendo os dados
with open(arquivo_csv, mode='r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    
    # Lê e imprime cada linha
    for linha in leitor:
        print(linha)