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

class EstrategiaDesconto:
    def calcula_desconto(self, valor_unitario):
        raise NotImplementedError

class DescontoNulo(EstrategiaDesconto):
    def calcula_desconto(self, valor_unitario):
        return 0.0

class Desconto10Porcento(EstrategiaDesconto):
    def calcula_desconto(self, valor_unitario):
        return valor_unitario * 0.1


# Exemplo de uso
produto_com_desconto_nulo = Produto(1, "Produto A", 10, 100, DescontoNulo())
produto_com_desconto_10porcento = Produto(2, "Produto B", 5, 200, Desconto10Porcento())

print("Detalhes do Produto com Desconto Nulo:")
produto_com_desconto_nulo.mostra_detalhes()
print("Valor do Desconto: R$", produto_com_desconto_nulo.calcula_desconto())

print("\nDetalhes do Produto com Desconto de 10%:")
produto_com_desconto_10porcento.mostra_detalhes()
print("Valor do Desconto: R$", produto_com_desconto_10porcento.calcula_desconto())
