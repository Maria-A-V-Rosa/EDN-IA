# Definindo o valor em reais que será convertido
valor_reais = 100.00  # Valor em reais

# Definindo as taxas de conversão
taxa_dolar = 5.60     # 1 dólar = 5.60 reais
taxa_euro = 6.60      # 1 euro = 6.60 reais

# Fazendo a conversão de reais para dólar
valor_dolar = valor_reais / taxa_dolar  # Divide o valor em reais pela taxa do dólar

# Fazendo a conversão de reais para euro
valor_euro = valor_reais / taxa_euro    # Divide o valor em reais pela taxa do euro

# Exibindo os resultados, formatando para duas casas decimais
print(f"Valor em dólares: US$ {valor_dolar:.2f}")  # Mostra o valor em dólar com 2 casas decimais
print(f"Valor em euros: € {valor_euro:.2f}")       # Mostra o valor em euro com 2 casas decimais