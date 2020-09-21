from ClasseForma import FormaGeométrica, Quadrado, Triângulo

o1 = FormaGeométrica('Azul')
o2 = Quadrado('Verde', 5)
o3 = Triângulo('Amarelo', 3, 2)
print(o1.calc_area())
print(o2.calc_area())
print(o3.calc_area())
