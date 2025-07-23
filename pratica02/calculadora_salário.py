# Entrada dos dados
numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor recebido por hora: "))

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Saída formatada
print(f"NÚMERO = {numero_funcionario}")
print(f"SALÁRIO = R$ {salario:.2f}")