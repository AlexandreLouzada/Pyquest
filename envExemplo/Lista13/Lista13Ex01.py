class Produto:
    def __init__(self, codigo, nome, quantidade, valor_unitario, estrategia_desconto):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.estrategia_desconto = estrategia_desconto

    def mostra_detalhes(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Valor Unitário: {self.valor_unitario}")

    def adiciona_estoque(self, quantidade):
        self.quantidade += quantidade

    def calcula_desconto(self):
        return self.estrategia_desconto.calcula_desconto(self.valor_unitario)

