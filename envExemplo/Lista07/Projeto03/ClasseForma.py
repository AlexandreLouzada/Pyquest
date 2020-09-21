class FormaGeométrica(object):
    def __init__(self, c):
        self.cor = c

    def calc_area(self):
        return 0


class Quadrado(FormaGeométrica):
    def __init__(self, c, l):
        super().__init__(c)
        self.lado = l

    def calc_area(self):
        return self.lado * self.lado


class Triângulo(FormaGeométrica):
    def __init__(self, c, b, a):
        super().__init__(c)
        self.base = b
        self.altura = a

    def calc_area(self):
        return self.base * self.altura / 2
