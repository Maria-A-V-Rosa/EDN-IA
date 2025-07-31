# Programa para calcular o preço final com desconto

# Entrada do usuário
preco_original = float(input("Informe o preço original do produto: R$ "))
percentual_desconto = float(input("Informe o percentual de desconto (%): "))

# Cálculo do desconto e do preço final
valor_desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - valor_desconto

# Exibição do resultado com duas casas decimais
print(f"Preço com desconto: R$ {preco_final:.2f}")