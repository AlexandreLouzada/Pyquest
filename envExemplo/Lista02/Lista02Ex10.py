"""
Elabore um programa que leia diversos números e ao final escreva:
a quantidade de números digitados, a quantidade de números pares,
a quantidade de números ímpares.
"""
quantidade = par = ímpar = 0
número = int(input("Número: "))

while número != 0:
    quantidade = quantidade + 1
    if número % 2 == 0:
        par += 1
    if número % 2 == 1:
        ímpar += 1
    número = int(input("Número: "))

print(f'O total de números digitados foi de {quantidade}')
print(f'A quantidade de números pares são {par}')
print(f'A quantidade de números ímpares são {ímpar}')