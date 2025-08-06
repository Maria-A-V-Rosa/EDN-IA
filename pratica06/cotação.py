import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"
        
        if chave in dados:
            info = dados[chave]
            valor_atual = info['bid']
            valor_max = info['high']
            valor_min = info['low']
            data_hora = info['create_date']
            
            print(f"Cotação {moeda}/BRL:")
            print(f"Valor atual: R$ {valor_atual}")
            print(f"Valor máximo do dia: R$ {valor_max}")
            print(f"Valor mínimo do dia: R$ {valor_min}")
            print(f"Última atualização: {data_hora}")
        else:
            print("Código da moeda inválido ou não encontrado.")
    else:
        print("Erro ao consultar a API.")

def main():
    moeda = input("Informe o código da moeda (ex: USD, EUR, GBP): ").strip().upper()
    if len(moeda) != 3:
        print("Código inválido. Deve ter 3 letras.")
        return
    consultar_cotacao(moeda)

if __name__ == "__main__":
    main()