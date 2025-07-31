from datetime import datetime

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Aproximação simples (não conta anos bissextos)
    return idade_dias

# Exemplo de uso
ano = int(input("Digite o ano de nascimento: "))
dias = calcular_idade_em_dias(ano)
print(f"Você tem aproximadamente {dias} dias de vida.")