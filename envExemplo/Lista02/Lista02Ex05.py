"""
Crie um programa que leia a altura de um número indeterminado de pessoas.
Ao final o programa deve informar o total de pessoas cadastradas, a quantidade
de pessoas com altura inferior a 1,60 metros; a quantidade de pessoas com altura
entre 1,60 metros e 1,80 metros e a quantidade de pessoas com altura superior a 1,80 metros.
"""
inf = sup = med = 0
altura= float(input('Digite sua altura: '))
while altura > 0:
    if altura < 1.6 :
        inf += 1
    elif altura > 1.8 :
        sup += 1
    else:
        med += 1
    altura= float(input('Digite sua altura: '))
total= inf + sup + med
print('As pessoas com altura menor que 1.60 são {}' .format(inf))
print('As pessoas com altura maior que 1.80 são {}' .format(sup))
print('As pessoas com altura entre 1.60 e 1.80 são {}' .format(med))
print('O total de pessoas cadastradas foi {}' .format(total))
