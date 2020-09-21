"""
Crie um programa que leia o nome e a altura de 10 pessoas e ao final escreva:
a altura média do grupo, o nome e a altura da pessoa mais alta.
"""
maior_altura = soma = media = 0

for cont in range(2):
    nome = input('Digite seu nome: ')
    altura = float(input('Digite sua altura: '))
    soma += altura
    if altura > maior_altura:
        maior_altura = altura
        nome_alto = nome

media = soma/2

print('A altura média é {:.2f}' .format(media))
print('{} é a pessoa mais alta'.format(nome_alto))
print('Sua altura é de {} metros'.format(maior_altura))
