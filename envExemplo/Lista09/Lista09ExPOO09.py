class Produto:
    def __init__(self, codigo, nome, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
    
    def mostrardetalhes(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
    
    def adicionarestoque(self, quantidade):
        self.quantidade += quantidade

class ProdutoEletronico(Produto):
    def __init__(self, codigo, nome, quantidade, marca):
        super().__init__(codigo, nome, quantidade)
        self.marca = marca
    
    def exibirmarca(self):
        print(f"Marca: {self.marca}")
        
    def mostrardetalhes(self):
        super().mostrardetalhes()
        self.exibirmarca()

# Exemplo de polimorfismo
produto1 = Produto(1, "Caneta", 10)
produto2 = ProdutoEletronico(2, "Smartphone", 5, "Apple")

produtos = [produto1, produto2]

for produto in produtos:
    produto.mostrardetalhes()
    print()
