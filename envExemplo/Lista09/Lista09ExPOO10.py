class Produto:
    def __init__(self, codigo, nome, quantidade, preco):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    
    def exibir_dados(self):
        print(f"Código: {self.codigo}\nNome: {self.nome}\nQuantidade: {self.quantidade}\nPreço: {self.preco}")

class ProdutoEletronico(Produto):
    def __init__(self, codigo, nome, quantidade, preco, voltagem):
        super().__init__(codigo, nome, quantidade, preco)
        self.voltagem = voltagem
    
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Voltagem: {self.voltagem}")

class Notebook(ProdutoEletronico):
    def __init__(self, codigo, nome, quantidade, preco, voltagem, marca):
        super().__init__(codigo, nome, quantidade, preco, voltagem)
        self.marca = marca
    
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Marca: {self.marca}")

produto = Produto("001", "Camisa", 5, 25.99)
produto.exibir_dados()
print("------")
eletronico = ProdutoEletronico("002", "Fone de Ouvido", 3, 89.90, "Bivolt")
eletronico.exibir_dados()
print("------")
notebook = Notebook("003", "Notebook Dell", 1, 3899.99, "110V", "Dell")
notebook.exibir_dados()
