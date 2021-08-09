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

print(f'o total de alunos é {total_alunos}')
print(f'a porcentagem de alunos é de {porcentmasc:.2f}%')
print(f'a porcentagem de alunas é de {porcentfemi:.2f}%')
