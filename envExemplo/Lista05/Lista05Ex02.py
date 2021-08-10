"""
Um programa que armazena em uma lista o nome, o sexo e a
nota dos alunos de uma turma. Ao final o programa deve
exibir a quantidade de alunos, a média da turma, os
nomes da mulheres e os dados dos alunos com nota superior
a média da turma.
"""

turma = list()
aluno = dict()
soma = media = 0

while True:
    aluno.clear()
    aluno['nome'] = str(input('Nome: '))
    while True:
        aluno['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if aluno['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    aluno['nota'] = float(input('nota: '))
    soma += aluno['nota']
    turma.append(aluno.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(turma)} alunos cadastradas.')
media = soma / len(turma)
print(f'B) A média da turma é: {media:5.2f}')
print('C) As mulheres cadastradas foram ', end='')
for posição in turma:
    if posição['sexo'] in 'Ff':
        print(f'{posição["nome"]} ', end='')
print()
print('D) Lista das alunos que estão acima da média: ')
for posição in turma:
    if posição['nota'] > media:
        print('    ', end='')
        for chave, valor in posição.items():
            print(f'{chave} = {valor}; ', end='')
        print()
print('<< ENCERRADO >>')

