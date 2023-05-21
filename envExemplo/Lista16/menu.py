import obter_cotacoes
import graficos

def exibir_menu():
    print("Escolha o tipo de gráfico:")
    print("1 - Barras")
    print("2 - Pizza")
    print("3 - Dispersão")
    print("0 - Sair")


def obter_cotacao_moedas():
    cotacoes = obter_cotacoes.obter_dados_cotacoes()
    dolar = cotacoes["USD"]
    euro = cotacoes["EUR"]
    libra = cotacoes["GBP"]
    print("Cotação das moedas em relação ao Real:")
    print(f"Dólar Americano (USD): {dolar}")
    print(f"Euro (EUR): {euro}")
    print(f"Libra Esterlina (GBP): {libra}")
    print()

    moedas = ["USD - Dólar", "EUR - Euro", "GBP - Libra"]
    valores = [dolar, euro, libra]

    while True:
        exibir_menu()
        opcao = input("Opção: ")

        if opcao == "1":
            graficos.exibir_grafico_barras(moedas, valores)
        elif opcao == "2":
            graficos.exibir_grafico_pizza(moedas, valores)
        elif opcao == "3":
            graficos.exibir_grafico_dispersao(moedas, valores)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Obtém as cotações de moedas e exibe o gráfico de acordo com a opção escolhida pelo usuário
obter_cotacao_moedas()

