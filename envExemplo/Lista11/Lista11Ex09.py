import tensorflow as tf

class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

produtos = [
    Produto('Camiseta', 29.99, 'Roupas'),
    Produto('Calça Jeans', 79.99, 'Roupas'),
    Produto('Tênis', 99.99, 'Calçados'),
    Produto('Smartphone', 1499.99, 'Eletrônicos'),
    Produto('Notebook', 3499.99, 'Eletrônicos'),
    Produto('Livro', 19.99, 'Livros')
]

# Converter a lista de produtos em tensores
nomes = tf.constant([p.nome for p in produtos])
precos = tf.constant([p.preco for p in produtos])
categorias = tf.constant([p.categoria for p in produtos])

# Calcular a média dos preços dos produtos
media_precos = tf.reduce_mean(precos)

# Filtrar os produtos por categoria
eletronicos = tf.boolean_mask(nomes, tf.equal(categorias, 'Eletrônicos'))

# Imprimir os resultados
print("Média dos preços dos produtos:", media_precos.numpy())
print("Produtos eletrônicos:", eletronicos.numpy())


