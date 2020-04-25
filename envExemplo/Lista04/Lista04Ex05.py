'''
Faça um programa que leia uma distância em
quilômetros e ao final calcule e informe a distância
convertida em metros
'''

def converte_metros(dist):
    return dist * 1000

# Programa principal
print('')
print('-' * 30)
distancia = float(input('Digite uma distância em Km: '))
print(f'Distância em metros: {converte_metros(distancia)}')
print('-' * 30)
