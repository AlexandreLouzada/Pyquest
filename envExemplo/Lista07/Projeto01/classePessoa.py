class Pessoa(object):
    def __init__(self, n, i, p):
        self.nome = n
        self.idade = i
        self.peso = p

    def __repr__(self):
        return f'{self.nome} tem {self.idade} anos e pesa {self.peso}Kg.'

    def aniversario(self):
        self.idade += 1
