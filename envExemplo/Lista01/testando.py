aprovados = 0
quantidade = 3

for contador in range(quantidade):
    aluno = input('digite seu nome:')
    nota = float(input(f'{aluno} digite sua nota:'))
    if nota > 7:
        aprovados += 1

porcentagem_aprovados = aprovados/quantidade * 100

print(f'Quantidade de pessoas aprovadas: {aprovados}')
print(f'Porcentagem de pessoas aprovadas: {porcentagem_aprovados:.2f}')


