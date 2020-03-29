"""
Construir um programa que leia a quantidade de alunos do sexo masculino,
do sexo feminino e a quantidade de alunos aprovados de uma turma e calcule,
armazene e imprima o total de alunos e a porcentagem de alunos do sexo masculino,
do sexo feminino e a porcentagem de alunos aprovados.
"""
sexo1 = int(input('digite a quantidade de alunos do sexo masculino:'))
sexo2 = int(input('digite a quantidade de alunos do sexo feminino:'))
totaldealunos= sexo1 + sexo2
porcentmasc = sexo1/totaldealunos*100
porcentfemi = sexo2/totaldealunos*100
print('o total de alunos é {}'.format(totaldealunos))
print('a porcentagem de alunos masculinos é de {:.2f}%'.format(porcentmasc))
print('a porcentagem de alunas femininas é de {:.2f}%'.format(porcentfemi))
