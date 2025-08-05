import csv

dados = [
    ["Nome", "Idade", "Cidade"],
    ["Maria", "30", "São Paulo"],
    ["João", "25", "Rio de Janeiro"],
    ["Ana", "22", "Curitiba"]
]

with open("pessoas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    for linha in dados:
        escritor.writerow(linha)

print("Arquivo CSV criado com sucesso!")