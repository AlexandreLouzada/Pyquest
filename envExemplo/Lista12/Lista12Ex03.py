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

