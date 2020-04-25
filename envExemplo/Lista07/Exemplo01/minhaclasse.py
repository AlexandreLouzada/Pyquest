class Pessoa(object):
    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.peso = 0
    def __repr__(self):
        return f'{self.nome} tem {self.idade} anos e pesa {self.peso}Kg.'
    def aniversario(self):
        self.idade += 1
