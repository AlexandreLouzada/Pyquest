class Produto:
    imposto = 0.1  # Atributo da classe

    def __init__(self, codigo, nome, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade

    def calcular_preco_com_imposto(self):
        return self.quantidade * self.imposto

    @staticmethod
    def metodo_estatico():
        print("Este é um método estático")

    @classmethod
    def metodo_de_classe(cls):
        print("Este é um método de classe")
        print("Acessando o imposto da classe:", cls.imposto)

produto = Produto(1, "Camiseta", 10)

print(produto.calcular_preco_com_imposto())  # Chamando um método de instância

Produto.metodo_estatico()  # Chamando um método estático diretamente na classe

Produto.metodo_de_classe()  # Chamando um método de classe diretamente na classe

