"""
A conversão de graus Farenheit para graus centígrados é obtida por :
C = 5/9 * (F -32). Faça um programa que calcule e escreva uma tabela
de centígrados em função de graus Farenheit, que variam de 100 a 150 de 1 em 1.
"""
for f in range (100, 151):
    c = (5/9) * (f - 32)
    print('{}°F é igual a {:.2f}°C. ' .format(f, c))

