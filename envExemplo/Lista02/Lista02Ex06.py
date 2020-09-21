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

print('Total de pessoas cadastradas ---------------> {}' .format(total))
print('Porcentagem de pessoas adultas -------------> {:.2f}' .format(menores))
print('Porcentagem de pessoas menores de idade ----> {:.2f}' .format(adultos))
