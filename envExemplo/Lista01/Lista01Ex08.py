"""
Sejam P(x1,y1) e Q(x2,y2) dois pontos quaisquer do plano. A sua distância é dada por:
D = ((x2 – x1)**2 + (y2 – y1)**2)**(1/2)
Elabore um programa que leia as coordenadas dos pontos “P” e “Q”, calcule e escreva
sua distância.aaaaaa
"""

x1 = int(input("Digite o valor de x1:"))
x2 = int(input("Digite o valor de x2:"))
y1 = int(input("Digite o valor de y1:"))
y2 = int(input("Digite o valor de y2:"))
resultado = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
print('{:.2f}'.format(resultado))

