class ItemVendavel:
    def calcular_preco(self):
        raise NotImplementedError("Método calcular_preco() não implementado.")

class Produto(ItemVendavel):
    def __init__(self, codigo, nome, quantidade, preco_unitario):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def calcular_preco(self):
        return self.quantidade * self.preco_unitario

produto = Produto(1, "Celular", 10, 1000)
print(produto.calcular_preco())

