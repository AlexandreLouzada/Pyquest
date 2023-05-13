class Produto:
    def __init__(self, codigo, nome, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade

    def mostrar_detalhes(self):
        print("Detalhes do Produto:")
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade

    def __str__(self):
        return f"Código: {self.codigo}\nNome: {self.nome}\nQuantidade: {self.quantidade}"

    def __eq__(self, other):
        if isinstance(other, Produto):
            return self.codigo == other.codigo
        return False

    def __lt__(self, other):
        if isinstance(other, Produto):
            return self.quantidade < other.quantidade
        raise TypeError("Incompatível com a comparação")

    def __len__(self):
        return self.quantidade


# Exemplo de uso dos métodos e atributos da classe Produto
produto1 = Produto(1, "Camiseta", 10)
produto2 = Produto(2, "Calça", 5)

produto1.mostrar_detalhes()  # Exibe os detalhes do produto1
produto2.mostrar_detalhes()  # Exibe os detalhes do produto2

print(len(produto1))  # Retorna a quantidade do produto1

produto1.adicionar_estoque(5)  # Adiciona 5 unidades ao estoque do produto1

print(produto1)  # Exibe a representação em string do produto1

print(produto1 == produto2)  # Compara se o produto1 é igual ao produto2
print(produto1 < produto2)   # Compara se o produto1 é menor que o produto2

