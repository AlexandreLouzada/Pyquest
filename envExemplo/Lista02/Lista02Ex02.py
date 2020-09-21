"""
Faça um programa que calcule e escreva no vídeo o somatório
dos números inteiros de 1 até 50.
"""
acumulador = 0
for contador in range(1, 51):
    acumulador += contador
print('O valor total dos números será... {}' .format(acumulador))
