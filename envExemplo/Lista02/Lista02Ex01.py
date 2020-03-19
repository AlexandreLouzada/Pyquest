"""
Faça um programa que leia o preço de 10 produtos.
Ao final escreva o somatório dos preços.
"""
soma= 0.0
for cont in range (10):
    preco = float(input('Digite o preço: '))
    soma += preco
print('O valor total será {:.2f}' .format(soma))
