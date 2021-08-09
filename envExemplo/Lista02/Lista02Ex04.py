"""
Elabore um programa que leia o sexo de um número indeterminado de pessoas.
Ao final escreva a quantidade de pessoas cadastradas e o total de pessoas
de cada sexo.
"""

total_feminino = total_masculino = total_geral = 0
condição = 1

while condição != 0:
    sexo = input('Digite seu sexo: ')
    sexo = sexo.upper()
    if sexo in 'MF':
        total_geral += 1
        if sexo == 'M':
            total_masculino += 1
        else:
            total_feminino += 1
    else:
        print('Valor inválido')
    print('-' * 20)
    condição = int(input('Digite 0 para sair: '))
    print('-' * 20)

print(f'O total de pessoas do sexo masculino : {total_masculino}')
print(f'O total de pessoas do sexo feminino  : {total_feminino}')
print(f'O total de pessoas do inteiro grupo  : {total_geral}')
