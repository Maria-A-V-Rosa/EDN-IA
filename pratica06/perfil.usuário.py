import requests

def gerar_perfil_usuario():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados['results'][0]

        nome = usuario['name']
        nome_completo = f"{nome['title']} {nome['first']} {nome['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("Perfil de usuário gerado:")
        print(f"Nome: {nome_completo}")
        print(f"Email: {email}")
        print(f"País: {pais}")
    else:
        print("Erro ao acessar a API. Código:", resposta.status_code)

if __name__ == "__main__":
    gerar_perfil_usuario()