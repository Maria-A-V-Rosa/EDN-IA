# Entrada de dados
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
total_vendas = float(input("Digite o total de vendas no mês: "))

# Cálculo da comissão e total
comissao = total_vendas * 0.15
total_receber = salario_fixo + comissao

# Saída formatada
print(f"TOTAL = R$ {total_receber:.2f}")