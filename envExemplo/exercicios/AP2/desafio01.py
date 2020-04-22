listagem= list()
pessoas= dict()
soma_altura = soma_idade = media_alt = media_id =0
while True:
    pessoas.clear()
    pessoas['código'] = int(input('Código: '))
    pessoas['nome'] = str(input('Nome: '))
    pessoas['altura'] = float(input('Altura: '))
    pessoas['idade'] = float(input('Idades: '))
    soma_altura += pessoas['altura']
    soma_idade += pessoas['idade']
    listagem.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

media_alt = soma_altura/len(listagem)
media_id = soma_idade/len(listagem)

print('-=' * 30)
print(f'Foram cadastradas: {len(listagem)} pessoas')
print(f'Média das alturas: {media_alt}')
print(f'Média das idades: {media_id}')
print('-=' * 30)


