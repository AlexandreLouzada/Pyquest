#decorator
class Produto:
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


class ProdutoDecorator:
    def __init__(self, produto):
        self.produto = produto

    def mostra_detalhes(self):
        self.produto.mostra_detalhes()

    def adiciona_estoque(self, quantidade):
        self.produto.adiciona_estoque(quantidade)


class ProdutoComDesconto(ProdutoDecorator):
    def mostra_detalhes(self):
        super().mostra_detalhes()
        print("Desconto aplicado: 10%")

    def adiciona_estoque(self, quantidade):
        super().adiciona_estoque(quantidade)


# Exemplo de uso
produto_base = Produto(1, "Produto A", 10, 100)
produto_decorado = ProdutoComDesconto(produto_base)

# Mostra os detalhes do produto com desconto
produto_decorado.mostra_detalhes()

# Adiciona estoque ao produto com desconto
produto_decorado.adiciona_estoque(5)

