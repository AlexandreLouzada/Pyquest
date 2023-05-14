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

class ProdutoComDesconto(Produto):
    def __init__(self, codigo, nome, quantidade, valor_unitario, desconto):
        super().__init__(codigo, nome, quantidade, valor_unitario)
        self.desconto = desconto

    def mostra_detalhes(self):
        super().mostra_detalhes()
        print(f"Desconto: {self.desconto}")

# Exemplo de uso
produto = Produto(1, "Produto A", 10, 100)
produto_com_desconto = ProdutoComDesconto(2, "Produto B", 5, 200, 0.1)

print("Detalhes do Produto:")
produto.mostra_detalhes()

print("\nDetalhes do Produto com Desconto:")
produto_com_desconto.mostra_detalhes()
