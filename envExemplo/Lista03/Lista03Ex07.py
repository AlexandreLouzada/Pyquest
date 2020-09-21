"""
Construa um programa que armazene números inteiros em um vetor de 10
posições, calcule o quadrado de cada elemento armazenado neste vetor
e armazene o resultado em um outro vetor. Ao final os dados do segundo
vetor devem ser exibidos no vídeo.
"""
lista = []
quadrado = []
for n in range(4):
    lista.append(int(input('Digite um número: ')))
    quadrado.append(lista[n] * lista[n])

print(f'Os números digitados foram     {lista}')
print(f'Seus respectivos quadrados são {quadrado}')
