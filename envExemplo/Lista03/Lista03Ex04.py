"""
Construa um programa usando vetores que leia o nome e a nota
de 10 alunos e ao final escreva: a nota média da turma;
o nome e a nota dos alunos com resultados superiores a nota média da turma.
"""
listnome = []
listnota = []
soma = media= 0
turma = 3
traço = 40
for ind in range(turma):
    listnome.append(input('Digite o nome: '))
    listnota.append(float(input('Digite a nota: ')))
    soma += listnota[ind]

media = soma/turma
print('-'* traço)
print('A média da turma é {:.2f}' .format(media))
print('-'*traço)
print('Alunos com nota superior a média da turma')
print('-'*traço)
for ind in range(turma):
    if listnota[ind] > media:
        print(f'{listnome[ind]:10} {listnota[ind]:.2f}')
print('-'*traço)
