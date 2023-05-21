class ProdutoFactory:
    def __init__(self, codigo, nome, quantidade, valor_unitario):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

    def mostra_detalhes(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Valor Unitário: {self.valor_unitario}")

    def adiciona_estoque(self, quantidade):
        self.quantidade += quantidade
        print(f"Estoque atualizado: {self.quantidade}")

class ProdutoFactoryMethod:
    def create_produto(self, tipo, codigo, nome, quantidade, valor_unitario):
        if tipo == "comum":
            return ProdutoFactory(codigo, nome, quantidade, valor_unitario)
        elif tipo == "premium":
            valor_unitario *= 1.2
            return ProdutoFactory(codigo, nome, quantidade, valor_unitario)

# Uso do ProdutoFactoryMethod
factory = ProdutoFactoryMethod()

# Criação de produtos usando o factory method
produto_comum = factory.create_produto("comum", 1, "Caneta", 50, 1.99)
produto_premium = factory.create_produto("premium", 2, "Caderno", 100, 5.99)

# Exibição dos detalhes dos produtos
produto_comum.mostra_detalhes()
produto_premium.mostra_detalhes()

# Adição de estoque aos produtos
produto_comum.adiciona_estoque(20)
produto_premium.adiciona_estoque(30)
