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
for c in range(0, tamanho_lista):
    vendas.append(int(input(f'   Quantas vendas na campanha {c + 1}? ')))

vendedor['venda'] = vendas[:]  # armazena a lista de vendas no dicionário
vendedor['total'] = sum(vendas)  # armazena o total de vendas no dicionário

print('-=' * 30)
print(vendedor)  # exibe a estrutura do dicionário
print('-=' * 30)

# exibe a estrutura do dicionário de modo detalhado
for k, v in vendedor.items():
    print(f'O campo {k} tem o valor {v}')

# exibe os dados obtidos e o total das vendas
print('-=' * 30)
print(f'O vendedor {vendedor["nome"]} fez {len(vendedor["venda"])} vendas.')

for i, v in enumerate(vendedor['venda']):
    print(f'    => Na campanha {i + 1}, fez {v} vendas.')
print(f'Foi um total de {vendedor["total"]} vendas.')
