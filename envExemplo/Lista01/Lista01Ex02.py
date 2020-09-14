"""
Construir um programa que leia a quantidade de alunos do sexo masculino,
do sexo feminino e a quantidade de alunos aprovados de uma turma e calcule,
armazene e imprima o total de alunos e a porcentagem de alunos do sexo masculino,
do sexo feminino e a porcentagem de alunos aprovados.
"""
quant_sexo_masculino = int(input('digite a quantidade de alunos do sexo masculino:'))
quant_sexo_feminino = int(input('digite a quantidade de alunos do sexo feminino:'))

total_alunos = quant_sexo_masculino + quant_sexo_feminino
porcentmasc = quant_sexo_masculino/total_alunos*100
porcentfemi = quant_sexo_feminino/total_alunos*100

print('o total de alunos é {}'.format(total_alunos))
print('a porcentagem de alunos é de {:.2f}%'.format(porcentmasc))
print('a porcentagem de alunas é de {:.2f}%'.format(porcentfemi))
