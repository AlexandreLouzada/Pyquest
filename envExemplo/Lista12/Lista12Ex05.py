#observer
class Produto:
    def __init__(self, codigo, nome, quantidade, valor_unitario):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.observers = []

    def adiciona_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notifica_observers(self):
        for observer in self.observers:
            observer.atualiza(self)

    def mostra_detalhes(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Valor Unitário: {self.valor_unitario}")

    def adiciona_estoque(self, quantidade):
        self.quantidade += quantidade
        self.notifica_observers()


class EstoqueObserver:
    def atualiza(self, produto):
        print(f"Estoque atualizado para o produto {produto.nome}: {produto.quantidade}")


# Exemplo de uso
produto = Produto(1, "Produto A", 10, 100)

estoque_observer = EstoqueObserver()
produto.adiciona_observer(estoque_observer)

produto.adiciona_estoque(5)
