"""
Elabore um programa que leia a idade de diversas pessoas e ao final informe:
o total de pessoas cadastradas, a porcentagem de pessoas com idade inferior
a 18 anos, a porcentagem de pessoas com idade igual ou superior a 18 anos.
"""

c = inf = sup = 0
idade = int(input('Digite sua idade: '))
while idade > 0:
    c += 1
    if idade < 18:
        inf += 1
    elif idade >= 18:
        sup += 1
    idade = int(input('Digite sua idade: '))
pessoasinf = inf/c * 100
pessoassup = sup/c * 100
print('O total de pessoas cadastradas {}' .format(c))
print('A porcentagem de pessoas com idade inferior a 18 anos é {:.2f}' .format(inf))
print('A porcentagem de pessoas com idade ou superior a 18 anos é {:2f}' .format(sup))
