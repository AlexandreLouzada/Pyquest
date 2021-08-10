listagem = list()
candidato = dict()

while True:
    candidato.clear()
    candidato['numero'] = int(input('Numero: '))
    candidato['nome'] = str(input('Nome: '))
    candidato['nota'] = float(input('nota: '))
    listagem.append(candidato.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break

print('-=' * 30)
print(f'Listagem por ordem de classificação dos {len(listagem)} candidatos:')
print('-=' * 30)
print()

ordena_nota = sorted(listagem, key=lambda chave: k['nota'], reverse=True)

for ind in listagem:
    for k, v in ind.items():
        print(f'{k} : {v} ', end='')
    print()
