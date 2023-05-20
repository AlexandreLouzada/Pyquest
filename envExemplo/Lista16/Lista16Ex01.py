import requests
import matplotlib.pyplot as plt

def obter_cotacoes():
    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data["rates"]
    else:
        print(f"Erro ao obter as cotações de moedas: {response.status_code}")
        return None

def obter_nome_moeda(sigla):
    nome_moedas = {
        "USD": "Dólar Americano",
        "EUR": "Euro",
        "GBP": "Libra Esterlina",
        "JPY": "Iene Japonês",
        "CAD": "Dólar Canadense",
    }
    return nome_moedas.get(sigla, sigla)

def exibir_graficos(cotacoes):
    if cotacoes:
        moedas = list(cotacoes.keys())[:5] # cinco principais moedas do mundo
        valores = list(cotacoes.values())[:5]

        # Converter as siglas para nomes de moedas compreensíveis
        nomes_moedas = [obter_nome_moeda(sigla) for sigla in moedas]

        # Gráfico de barras
        plt.figure(figsize=(10, 6))
        plt.bar(nomes_moedas, valores)
        plt.title("Cotação das Moedas em Relação ao Real")
        plt.xlabel("Moedas")
        plt.ylabel("Valor em Reais")
        plt.xticks(rotation=45)
        plt.show()

        # Gráfico de pizza
        plt.figure(figsize=(8, 8))
        plt.pie(valores, labels=nomes_moedas, autopct='%1.1f%%')
        plt.title("Distribuição das Cotações das Moedas")
        plt.legend(loc='upper right')
        plt.show()

        # Gráfico de linha
        plt.figure(figsize=(10, 6))
        plt.plot(nomes_moedas, valores, marker='o')
        plt.title("Variação das Cotações das Moedas")
        plt.xlabel("Moedas")
        plt.ylabel("Valor em Reais")
        plt.xticks(rotation=45)
        plt.show()

        # Gráfico de dispersão
        plt.figure(figsize=(10, 6))
        plt.scatter(nomes_moedas, valores, color='red')
        plt.title("Dispersão das Cotações das Moedas")
        plt.xlabel("Moedas")
        plt.ylabel("Valor em Reais")
        plt.xticks(rotation=45)
        plt.show()

        # Gráfico de área
        plt.figure(figsize=(10, 6))
        plt.stackplot(nomes_moedas, valores, labels=nomes_moedas)
        plt.title("Variação das Cotações das Moedas")
        plt.xlabel("Moedas")
        plt.ylabel("Valor em Reais")
        plt.xticks(rotation=45)
        plt.legend(loc='upper left')
        plt.show()
    else:
        print("Não foi possível obter as cotações de moedas.")

# Obtém as cotações de moedas
cotacoes = obter_cotacoes()

# Exibe os gráficos das cotações de moedas
exibir_graficos(cotacoes)
