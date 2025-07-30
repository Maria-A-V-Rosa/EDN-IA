print("Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número.\n")

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break

    if len(senha) < 8:
        print("Senha fraca: deve ter pelo menos 8 caracteres.\n")
        continue

    if not any(char.isdigit() for char in senha):
        print("Senha fraca: deve conter pelo menos um número.\n")
        continue

    print("Senha forte! ✅")
    break