import matplotlib.pyplot as plt

def exibir_grafico_barras(moedas, valores):
    plt.bar(moedas, valores)
    plt.xlabel("Moedas")
    plt.ylabel("Cotação em relação ao Real")
    plt.title("Cotação das moedas em relação ao Real")
    plt.show()

def exibir_grafico_pizza(moedas, valores):
    plt.pie(valores, labels=moedas, autopct="%1.1f%%")
    plt.title("Proporção das moedas em relação ao Real")
    plt.show()

def exibir_grafico_dispersao(moedas, valores):
    plt.scatter(moedas, valores)
    plt.xlabel("Moedas")
    plt.ylabel("Cotação em relação ao Real")
    plt.title("Relação entre as cotações das moedas em relação ao Real")
    plt.show()
