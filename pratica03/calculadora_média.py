# Entrada das 4 notas com uma casa decimal
n1, n2, n3, n4 = map(float, input("Digite as 4 notas separadas por espaço: ").split())

# Cálculo da média ponderada
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

# Mostra a média inicial
print(f"Media: {media:.1f}")

# Decisão baseada na média
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    # Entrada da nota do exame
    nota_exame = float(input("Digite a nota do exame: "))
    print(f"Nota do exame: {nota_exame:.1f}")
    
    # Recalcula a média
    media_final = (media + nota_exame) / 2

    # Resultado final após o exame
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    # Exibe a média final
    print(f"Media final: {media_final:.1f}")