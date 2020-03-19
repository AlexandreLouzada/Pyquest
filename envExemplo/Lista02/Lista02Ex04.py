"""
Elabore um programa que leia o sexo de um número indeterminado de pessoas.
Ao final escreva a quantidade de pessoas cadastradas e o total de pessoas
de cada sexo.
"""

totalF = totalM = total = 0
c = i = 1
while (i != 0):
    sexo= input('Digite seu sexo: ')
    total= total + 1
    if (sexo == 'M'):
        totalM+= 1
    if (sexo == 'F'):
        totalF+= 1
    i= int(input('Digite 0 para sair'))
print('O total masculino será {}'.format(totalM))
print('O total feminino será {}' .format(totalF))
print('O total de pessoas vai ser {}' .format(total))
