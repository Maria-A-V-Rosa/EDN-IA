# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Verifica se a idade está dentro de uma faixa aceitável
if 0 <= idade <= 130:
    if idade <= 12:
        categoria = "Criança"
    elif idade <= 17:
        categoria = "Adolescente"
    elif idade <= 59:
        categoria = "Adulto"
    else:  # idade entre 60 e 130
        categoria = "Idoso"
else:
    categoria = "Idade inválida"

# Exibe o resultado
print(f"Classificação: {categoria}")