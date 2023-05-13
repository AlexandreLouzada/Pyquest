class Categoria:
    def __init__(self, nome):
        self.nome = nome

class Produto:
    def __init__(self, codigo, nome, quantidade, categoria):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.categoria = categoria

    def mostrar_detalhes(self):
        print("Detalhes do Produto:")
        print("Código:", self.codigo)
        print("Nome:", self.nome)
        print("Quantidade:", self.quantidade)
        print("Categoria:", self.categoria.nome)

# Criando uma instância da classe Categoria
categoria = Categoria("Eletrônicos")

# Criando uma instância da classe Produto, passando a categoria como argumento
produto = Produto(1, "Celular", 10, categoria)

# Chamando o método mostrar_detalhes do produto
produto.mostrar_detalhes()

