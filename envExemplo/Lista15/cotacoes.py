import requests

def obter_cotacao_moedas():
    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data["rates"]
    else:
        print(f"Erro ao obter as cotações de moedas: {response.status_code}")
        return None
