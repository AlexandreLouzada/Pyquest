import pandas as pd

# Define a lista de dicionários com as informações das cidades
cidades = [
    {'nome': 'São Paulo', 'estado': 'SP', 'populacao': 12325232},
    {'nome': 'Rio de Janeiro', 'estado': 'RJ', 'populacao': 6747815},
    {'nome': 'Salvador', 'estado': 'BA', 'populacao': 2886698},
    {'nome': 'Belo Horizonte', 'estado': 'MG', 'populacao': 2523794},
    {'nome': 'Fortaleza', 'estado': 'CE', 'populacao': 2686612},
    {'nome': 'Manaus', 'estado': 'AM', 'populacao': 2219580},
    {'nome': 'Curitiba', 'estado': 'PR', 'populacao': 1948626},
    {'nome': 'Recife', 'estado': 'PE', 'populacao': 1645727},
    {'nome': 'Porto Alegre', 'estado': 'RS', 'populacao': 1488252},
    {'nome': 'Belém', 'estado': 'PA', 'populacao': 1499641}
]

# Cria um DataFrame do pandas a partir da lista de dicionários
cidades_df = pd.DataFrame(cidades)

# Ordena o DataFrame pela coluna "populacao" em ordem decrescente
sorted_cidades_df = cidades_df.sort_values(by='populacao', ascending=False)

# Imprime as cinco cidades com a maior população
print(sorted_cidades_df.head(5)['nome'])
