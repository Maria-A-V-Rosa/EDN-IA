# Calculadora de Número Inteiro

# Lê quatro valores inteiros, cada um em uma linha diferente
A = int(input())  # Lê o primeiro número inteiro
B = int(input())  # Lê o segundo número inteiro
C = int(input())  # Lê o terceiro número inteiro
D = int(input())  # Lê o quarto número inteiro

# Calcula a diferença entre o produto de A e B e o produto de C e D
DIFERENCA = (A * B) - (C * D)

# Exibe o resultado no formato solicitado, com a mensagem em letras maiúsculas
print(f"DIFERENCA = {DIFERENCA}")
