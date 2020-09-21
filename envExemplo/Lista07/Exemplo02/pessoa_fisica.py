from pessoa import Pessoa


class Pessoafisica(Pessoa):
    def __init__(self, cpf, nome, idade):
        super().__init__(nome, idade)
        self.cpf = cpf

    def getcpf(self):
        return self.cpf

    def setcpf(self, cpf):
        self.cpf = cpf
