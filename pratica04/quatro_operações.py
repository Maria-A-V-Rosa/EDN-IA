def calculadora():
    while True:
        try:
            # Solicita o primeiro número
            num1 = float(input("Digite o primeiro número: "))
        except ValueError:
            print("Erro: O valor digitado não é um número válido.\n")
            continue

        try:
            # Solicita o segundo número
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: O valor digitado não é um número válido.\n")
            continue

        # Solicita a operação
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao not in ['+', '-', '*', '/']:
            print("Erro: Operação inválida. Digite apenas +, -, * ou /.\n")
            continue

        try:
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError
                resultado = num1 / num2

            # Mostra o resultado e encerra o programa
            print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
            break

        except ZeroDivisionError:
            print("Erro: Não é possível dividir por zero.\n")

# Executa a calculadora
calculadora()