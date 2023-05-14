class Produto:
    def __init__(self, codigo, nome, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade

    def mostrar_detalhes(self):
        print("Código:", self.codigo)
        print("Nome:", self.nome)
        print("Quantidade:", self.quantidade)

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade

produto = Produto(1, "Celular", 10)

print(produto.__class__.__name__)  # Saída: Produto