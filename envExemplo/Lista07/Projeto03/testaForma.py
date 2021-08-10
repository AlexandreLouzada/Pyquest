from ClasseForma import FormaGeométrica, Quadrado, Triângulo

objeto1 = FormaGeométrica('Azul')
objeto2 = Quadrado('Verde', 5)
objeto3 = Triângulo('Amarelo', 3, 2)
print(objeto1.calc_area())
print(objeto2.calc_area())
print(objeto3.calc_area())
