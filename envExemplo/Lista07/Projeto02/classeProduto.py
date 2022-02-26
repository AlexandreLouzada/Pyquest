class Produto(object):
    def __init__(self):
        self.__fabricante = ''
        self.__preço = 0.0

    def getFabricante(self):
        return f'{self.__fabricante:}'

    def setFabricante(self,f):
        self.__fabricante = f

    def getPreço(self):
        return f'R${self.__preço:.2f}'

    def setPreço(self, p):
        if p >= 0:
            self.__preço = p

