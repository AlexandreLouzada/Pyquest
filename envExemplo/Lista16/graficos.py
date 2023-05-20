import matplotlib.pyplot as plt
from nome_moedas import obter_nome_moeda


def exibir_grafico_barras(moedas, valores):
    plt.figure(figsize=(10, 6))
    plt.bar([obter_nome_moeda(moeda) for moeda in moedas], valores)
    plt.title("Cotação das Moedas em Relação ao Real")
    plt.xlabel("Moedas")
    plt.ylabel("Valor em Reais")
    plt.xticks(rotation=45)
    plt.show()


def exibir_grafico_pizza(moedas, valores):
    plt.figure(figsize=(8, 8))
    plt.pie(valores, labels=[obter_nome_moeda(moeda) for moeda in moedas], autopct='%1.1f%%')
    plt.title("Distribuição das Cotações das Moedas")
    plt.legend(loc='upper right')
    plt.show()


def exibir_grafico_linha(moedas, valores):
    plt.figure(figsize=(10, 6))
    plt.plot([obter_nome_moeda(moeda) for moeda in moedas], valores, marker='o')
    plt.title("Variação das Cotações das Moedas")
    plt.xlabel("Moedas")
    plt.ylabel("Valor em Reais")
    plt.xticks(rotation=45)
    plt.show()


def exibir_grafico_dispersao(moedas, valores):
    plt.figure(figsize=(10, 6))
    plt.scatter([obter_nome_moeda(moeda) for moeda in moedas], valores, color='red')
    plt.title("Dispersão das Cotações das Moedas")
    plt.xlabel("Moedas")
    plt.ylabel("Valor em Reais")
    plt.xticks(rotation=45)
    plt.show()


def exibir_grafico_area(moedas, valores):
    plt.figure(figsize=(10, 6))
    plt.stackplot([obter_nome_moeda(moeda) for moeda in moedas], valores, labels=[obter_nome_moeda(moeda) for moeda in moedas])
    plt.title("Variação das Cotações das Moedas")
    plt.xlabel("Moedas")
    plt.ylabel("Valor em Reais")
    plt.xticks(rotation=45)
    plt.legend(loc='upper left')
    plt.show()
