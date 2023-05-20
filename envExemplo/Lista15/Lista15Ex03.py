import requests

def obter_cotacao_moedas():
    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        cotacoes = data["rates"]
        dolar = cotacoes["USD"]
        euro = cotacoes["EUR"]
        libra = cotacoes["GBP"]
        print("Cotação das moedas em relação ao Real:")
        print(f"Dólar Americano (USD): {dolar}")
        print(f"Euro (EUR): {euro}")
        print(f"Libra Esterlina (GBP): {libra}")
        print()
    else:
        print(f"Erro ao obter as cotações de moedas: {response.status_code}")
        print()

# Obtém as cotações de moedas
obter_cotacao_moedas()

