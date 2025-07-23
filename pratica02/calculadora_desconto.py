# Nome do produto
nome_produto = "Camiseta"

# Preço original do produto
preco_original = 50.00

# Porcentagem de desconto (em %)
porcentagem_desconto = 20

# Cálculo do valor do desconto (20% de 50 reais)
valor_desconto = (porcentagem_desconto / 100) * preco_original

# Cálculo do preço final com o desconto aplicado
preco_final = preco_original - valor_desconto

# Exibição dos resultados 
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")