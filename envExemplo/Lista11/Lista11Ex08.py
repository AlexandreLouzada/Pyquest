from sklearn.cluster import KMeans
import numpy as np

class Produto:
    def __init__(self, nome, preco, peso):
        self.nome = nome
        self.preco = preco
        self.peso = peso

produtos = [
    Produto('Produto 1', 60.50, 0.70),
    Produto('Produto 2', 25.00, 0.50),
    Produto('Produto 3', 5.99, 0.20),
    Produto('Produto 4', 50.00, 0.75),
    Produto('Produto 5', 15.99, 0.30),
    Produto('Produto 6', 8.75, 0.15)
]

# Criar um array NumPy com os preços e pesos dos produtos
X = np.array([[p.preco, p.peso] for p in produtos])

# Executar o algoritmo de k-means com k=2
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

# Obter os rótulos de cada produto
labels = kmeans.labels_

# Imprimir os grupos de produtos
for i in range(2):
    print("Grupo", i+1, ":")
    for j in range(len(produtos)):
        if labels[j] == i:
            print("-", produtos[j].nome)


