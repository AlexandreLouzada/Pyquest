"""
Faça um programa que leia o preço de 10 produtos.
Ao final escreva o somatório dos preços.
"""
soma = 0.0
for cont in range(4):
    preço = float(input('Digite o preço: '))
    soma += preço

print(f'O valor total será {soma:.2f}')