def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta com base no valor da conta e na porcentagem desejada.

    Parâmetros:
        valor_conta (float): O valor total da conta.
        porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%).

    Retorna:
        float: O valor da gorjeta calculada.
    """
    return valor_conta * (porcentagem_gorjeta / 100)

# Exemplo de uso
valor = float(input("Informe o valor total da conta: R$ "))
porcentagem = float(input("Informe a porcentagem da gorjeta: "))

gorjeta = calcular_gorjeta(valor, porcentagem)
print(f"Você deve deixar R${gorjeta:.2f} de gorjeta.")