import requests

def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" in dados:
            print("CEP não encontrado.")
            return
        print(f"Logradouro: {dados.get('logradouro', 'Não informado')}")
        print(f"Bairro: {dados.get('bairro', 'Não informado')}")
        print(f"Cidade: {dados.get('localidade', 'Não informado')}")
        print(f"Estado: {dados.get('uf', 'Não informado')}")
    else:
        print("Erro ao consultar o CEP.")

def main():
    cep = input("Digite o CEP (somente números): ").strip()
    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido. Deve conter 8 números.")
        return
    consulta_cep(cep)

if __name__ == "__main__":
    main()