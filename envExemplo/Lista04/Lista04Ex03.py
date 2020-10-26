"""
Faça um programa que leia a largura e o comprimento
de um terreno e ao final informa a área do terreno.
"""


def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {area_terreno}m².')


# Programa principal
print('Controle de Terrenos')
print('-' * 20)
largura_terreno = float(input('LARGURA (m): '))
comprimento_terreno = float(input('COMPRIMENTO (m): '))
area(largura_terreno, comprimento_terreno)
