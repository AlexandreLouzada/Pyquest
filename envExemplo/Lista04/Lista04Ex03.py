"""
Faça um programa que leia a largura e o comprimento
de um terreno e ao final informa a área do terreno.
"""


def area(larg, comp):
    area_terreno = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {area_terreno}m².')


# Programa principal
print('Controle de Terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
