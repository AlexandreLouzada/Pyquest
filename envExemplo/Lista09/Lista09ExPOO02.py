class Frete:
    def calcular_frete(self):
        return 10

class Imposto:
    def calcular_imposto(self):
        return 5

class Produto(Frete, Imposto):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_preco_total(self):
        return self.preco + self.calcular_frete() + self.calcular_imposto()
