"""
Faça um programa que leia a idade de 10 pessoas.
Ao final escreva a média das idades.
"""
soma = 0
media = 0.0
for cont in range(10):
    idade = int(input('Digite sua idade: '))
    soma += idade
media = soma/10
print(f'A média das idades é {media:.2f}')