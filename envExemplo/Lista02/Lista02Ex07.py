"""
Faça um programa que leia vários números inteiros e ao final escreva o maior.
"""
num = int(input('Numero: '))
maior = num

while num != 0:
    if num > maior:
        maior = num
    num = int(input('Numero: '))

print(f'O número maior é: {maior}')
