"""
Crie um programa que leia a altura de um número indeterminado de pessoas.
Ao final o programa deve informar o total de pessoas cadastradas, a quantidade
de pessoas com altura inferior a 1,60 metros; a quantidade de pessoas com altura
entre 1,60 metros e 1,80 metros e a quantidade de pessoas com altura superior a 1,80 metros.
"""
inferior = superior = medio = 0
altura = float(input('Digite sua altura: '))

while altura > 0:
    if altura < 1.6:
        inferior += 1
    elif altura > 1.8:
        superior += 1
    else:
        medio += 1
    altura= float(input('Digite sua altura: '))

total= inferior + superior + medio

print('-*-' * 15)
print(f'Pessoas com altura menor que 1.60 ------> {inferior}')
print(f'Pessoas com altura maior que 1.80 ------> {superior}')
print(f'Pessoas com altura entre 1.60 e 1.80 ---> {medio}')
print(f'Total de pessoas cadastradas -----------> {total}')
print(f'-*-' * 15)
