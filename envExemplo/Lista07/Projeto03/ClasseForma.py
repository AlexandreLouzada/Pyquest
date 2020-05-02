class FormaGeométrica(object):
    def __init__(self, c):
        self.cor = c

    def calcÁrea(self):
        return 0

class Quadrado(FormaGeométrica):
    def __init__(self, c, l):
        super().__init__(c)
        self.lado = l

    def calcÁrea(self):
       return self.lado * self.lado

class Triângulo(FormaGeométrica):
    def __init__(self, c, b, a):
        super().__init__(c)
        self.base = b
        self.altura = a

    def calcÁrea(self):
        return self.base * self.altura / 2
