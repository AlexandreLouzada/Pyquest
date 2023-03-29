class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError("Idade não pode ser negativa")
        self._idade = idade

pessoa = Pessoa("ana", 30)
print(pessoa.nome)   # Ana
print(pessoa.idade)  # 30

pessoa.nome = "maria"
pessoa.idade = -10   # ValueError: Idade não pode ser negativa
