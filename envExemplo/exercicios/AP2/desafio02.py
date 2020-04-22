listagem= list()
produtos = dict()
soma_valor = media_valor = 0
while True:
    produtos.clear()
    produtos['código'] = int(input('Código: '))
    produtos['nome'] = str(input('Nome: '))
    produtos['preço'] = float(input('Preço:'))
    soma_valor += produtos['preço']
    listagem.append(produtos.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

media_valor = soma_valor/len(listagem)

print('-=' * 30)
print(f'Foram cadastradas: {len(listagem)} produtos')
print(f'Média dos preços: {media_valor}')
print('-=' * 30)
print()

print('Produtos superiores a média:')
for p in listagem:
    if p['preço'] >= media_valor:
        print(f'Produto: {p["nome"]}')
print()
