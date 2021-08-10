"""
Faça um programa que leia o nome de um vendedor, a
quantidade de campanhas de vendas em que o vendedor
participou e a quantidade de vendas que realizou em
cada campanha. Ao final o programa deve informar o
total de vendas que o vendedor obteve.
"""
vendedor = dict()  # dicionário para armazenar os dados do vendedor
vendas = list()  # lista de vendas de cada campanha

# obtém nome do vendedor
vendedor['nome'] = str(input('Nome do vendedor: '))

# obtém tamanho da lista
tamanho_lista = int(input(f'Número de campanhas que {vendedor["nome"]} participou: '))

# obtém a venda de cada campanha e insere na lista de vendas
for contador in range(0, tamanho_lista):
    vendas.append(int(input(f'   Quantas vendas na campanha {contador + 1}? ')))

vendedor['venda'] = vendas[:]  # armazena a lista de vendas no dicionário
vendedor['total'] = sum(vendas)  # armazena o total de vendas no dicionário

print('-=' * 30)
print(vendedor)  # exibe a estrutura do dicionário
print('-=' * 30)

# exibe a estrutura do dicionário de modo detalhado
for chave, valor in vendedor.items():
    print(f'O campo {chave} tem o valor {valor}')

# exibe os dados obtidos e o total das vendas
print('-=' * 30)
print(f'O vendedor {vendedor["nome"]} fez {len(vendedor["venda"])} vendas.')

for campanha, venda in enumerate(vendedor['venda']):
    print(f'    => Na campanha {campanha + 1}, fez {venda} vendas.')
print(f'Foi um total de {vendedor["total"]} vendas.')
