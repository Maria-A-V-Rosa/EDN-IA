# Solicita os dados do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Verifica se os valores são válidos
if peso <= 0 or altura <= 0:
    print("Peso ou altura inválidos.")
else:
    # Calcula o IMC
    imc = peso / (altura ** 2)

    # Classificação do IMC
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"

    # Exibe o resultado com duas casas decimais
    print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")