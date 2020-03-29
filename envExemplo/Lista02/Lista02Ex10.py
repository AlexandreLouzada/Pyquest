"""
Elabore um programa que leia diversos números e ao final escreva:
a quantidade de números digitados, a quantidade de números pares,
a quantidade de números ímpares.
"""
quant = par = ímpar = 0
num = int(input("Número: "))

while num != 0:
    quant = quant + 1
    if num % 2 == 0:
        par = par + 1
    if num % 2 == 1:
        ímpar = ímpar + 1
    num = int(input("Número: "))
print('O total de números digitados foi de {}' .format(quant))
print('A quantidade de números pares são {}' .format(par))
print('A quantidade de números ímpares são {}' .format(ímpar))
