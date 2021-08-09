"""
Elabore um programa que leia a idade de diversas pessoas e ao final informe:
o total de pessoas cadastradas, a porcentagem de menores (pessoas com idade inferior
a 18 anos), a porcentagem de adultos (pessoas com idade igual ou superior a 18 anos).
"""

total = menores = adultos = 0
idade = int(input('Digite sua idade: '))
while idade > 0:
    total += 1
    if idade < 18:
        menores += 1
    elif idade >= 18:
        adultos += 1
    idade = int(input('Digite sua idade: '))

porcentagem_menores = menores/total * 100
porcentagem_adultos = adultos/total * 100

print(f'Total de pessoas cadastradas ---------------> {total}')
print(f'Porcentagem de pessoas adultas -------------> {menores:.2f}')
print(f'Porcentagem de pessoas menores de idade ----> {adultos:.2f}')
