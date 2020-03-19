"""
Crie um programa que leia o nome e a altura de 10 pessoas e ao final escreva:
a altura média do grupo, o nome e a altura da pessoa mais alta.
"""
maior = soma = media = 0
for cont in range (10):
    nome = input('Digite seu nome: ')
    altura = float(input('Digite sua altura: '))
    soma += altura
    if altura > maior:
        m_alta = altura
        n_alta = nome
media = soma/10
print('A altura média é {:.2f}' .format(media))
print('{} é a pessoa mais alta e tem {:.2f} de altura'.format(n_alta,m_alta))
