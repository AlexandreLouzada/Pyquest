from obter_cotacoes import obter_cotacoes
from graficos import (
    exibir_grafico_barras,
    exibir_grafico_pizza,
    exibir_grafico_linha,
    exibir_grafico_dispersao,
    exibir_grafico_area
)

def exibir_menu():
    print("=== Menu ===")
    print("1. Gráfico de Barras")
    print("2. Gráfico de Pizza")
    print("3. Gráfico de Linha")
    print("4. Gráfico de Dispersão")
    print("5. Gráfico de Área")
    print("0. Sair")

def selecionar_opcao():
    opcao = input("Selecione uma opção: ")
    return opcao

def exibir_grafico(opcao, cotacoes):
    moedas = list(cotacoes.keys())[:5]
    valores = list(cotacoes.values())[:5]

    if opcao == "1":
        exibir_grafico_barras(moedas, valores)
    elif opcao == "2":
        exibir_grafico_pizza(moedas, valores)
    elif opcao == "3":
        exibir_grafico_linha(moedas, valores)
    elif opcao == "4":
        exibir_grafico_dispersao(moedas, valores)
    elif opcao == "5":
        exibir_grafico_area(moedas, valores)
    else:
        print("Opção inválida.")

def main():
    cotacoes = obter_cotacoes()

    if cotacoes:
        while True:
            exibir_menu()
            opcao = selecionar_opcao()

            if opcao == "0":
                break

            exibir_grafico(opcao, cotacoes)
    else:
        print("Não foi possível obter as cotações de moedas.")

if __name__ == "__main__":
    main()
