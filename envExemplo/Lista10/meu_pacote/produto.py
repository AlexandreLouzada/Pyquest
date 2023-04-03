class Produto:
    def __init__(self, codigo, nome, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade

    def mostrar_detalhes(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade
        print(f"{quantidade} unidades adicionadas ao estoque.")

