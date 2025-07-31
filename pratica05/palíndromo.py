def verificar_palindromo(texto):
    texto_limpo = ''
    for c in texto:
        if c.isalnum():  # mantém apenas letras e números
            texto_limpo += c.lower()

    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# Exemplo de uso
frase = input("Digite uma palavra ou frase: ")
resultado = verificar_palindromo(frase)
print(f"É palíndromo? {resultado}")