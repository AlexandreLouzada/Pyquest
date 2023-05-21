import requests

def obter_dados_cotacoes():
    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["rates"]
    else:
        raise Exception(f"Erro ao obter as cotações de moedas: {response.status_code}")
