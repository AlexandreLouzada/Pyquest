"""
Construa um programa usando vetores que leia o nome e a nota
de 10 alunos e ao final escreva: a nota média da turma;
o nome e a nota dos alunos com resultados superiores a nota média da turma.
"""
nome = []
nota = []
soma = media = 0
turma = 3
traço = 40

for indice in range(turma):
    nome.append(input('Digite o nome: '))
    nota.append(float(input('Digite a nota: ')))
    soma += nota[indice]

media = soma/turma
print('-' * traço)
print('A média da turma é {:.2f}' .format(media))
print('-'*traço)
print('Alunos com nota superior a média da turma')
print('-'*traço)

for indice in range(turma):
    if nota[indice] > media:
        print(f'{nome[indice]:10} {nota[indice]:.2f}')

print('-' * traço)
