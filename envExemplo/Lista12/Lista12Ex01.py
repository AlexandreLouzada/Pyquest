class ProdutoSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

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

# Uso do ProdutoSingleton
produto1 = ProdutoSingleton(1, "Caneta", 50, 1.99)
produto2 = ProdutoSingleton(2, "Caderno", 100, 5.99)

produto1.mostra_detalhes()
produto2.mostra_detalhes()

produto1.adiciona_estoque(20)
produto2.adiciona_estoque(30)