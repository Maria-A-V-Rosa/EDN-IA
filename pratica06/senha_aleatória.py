import random
import string

print("Começou o programa")

tamanho = input("Informe o tamanho da senha desejada: ")
print(f"Tamanho recebido: {tamanho}")

if not tamanho.isdigit() or int(tamanho) <= 0:
    print("Número inválido, precisa ser inteiro maior que zero.")
else:
    tamanho = int(tamanho)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    print("Senha gerada:", senha)

print("Fim do programa")