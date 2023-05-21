import requests
import matplotlib.pyplot as plt

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


        # Gráfico de barras
        moedas = ["USD - Dólar", "EUR - Euro", "GBP - Libra"]
        #moedas = ["USD", "EUR", "GBP"]
        valores = [dolar, euro, libra]

        opcao = input("Escolha o tipo de gráfico (1 - Barras, 2 - Linhas, 3 - Pizza, 4 - Dispersão): ")
        
        if opcao == "1":
            plt.bar(moedas, valores)
            plt.xlabel("Moedas")
            plt.ylabel("Cotação em relação ao Real")
            plt.title("Cotação das moedas em relação ao Real")
            plt.show()
 
        elif opcao == "2":
            # Gráfico de pizza

            plt.pie(valores, labels=moedas, autopct="%1.1f%%")
            plt.title("Proporção das moedas em relação ao Real")
            plt.show()

            plt.scatter(moedas, valores)
            plt.xlabel("Moedas")
            plt.ylabel("Cotação em relação ao Real")
            plt.title("Relação entre as cotações das moedas em relação ao Real")
            plt.show()
            
        elif opcao == "3":
            # Gráfico de dispersão
 
            plt.scatter(moedas, valores)
            plt.xlabel("Moedas")
            plt.ylabel("Cotação em relação ao Real")
            plt.title("Relação entre as cotações das moedas em relação ao Real")
            plt.show()

        else:
            print("Opção inválida.")

    else:
        print(f"Erro ao obter as cotações de moedas: {response.status_code}")
        print()

# Obtém as cotações de moedas e exibe o gráfico de acordo com a opção escolhida pelo usuário
obter_cotacao_moedas()
