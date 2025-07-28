# Recebe os dados do usuário
temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

# Conversão
resultado = None

if origem == destino:
    resultado = temperatura
elif origem == "C":
    if destino == "F":
        resultado = temperatura * 9/5 + 32
    elif destino == "K":
        resultado = temperatura + 273.15
elif origem == "F":
    if destino == "C":
        resultado = (temperatura - 32) * 5/9
    elif destino == "K":
        resultado = (temperatura - 32) * 5/9 + 273.15
elif origem == "K":
    if destino == "C":
        resultado = temperatura - 273.15
    elif destino == "F":
        resultado = (temperatura - 273.15) * 9/5 + 32

# Resultado
if resultado is not None:
    print(f"{temperatura:.2f}°{origem} = {resultado:.2f}°{destino}")
else:
    print("Unidade inválida. Use apenas C, F ou K.")