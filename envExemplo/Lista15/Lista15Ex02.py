import requests

# Função para obter a população de um estado pelo seu código
def obter_populacao_estado(codigo_estado):
    url = f'https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/{codigo_estado}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erro na resposta
        data = response.json()
        return data['projecao']['populacao']
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter a população do estado {codigo_estado}: {e}")
    except (KeyError, ValueError) as e:
        print(f"Erro ao processar os dados da API para o estado {codigo_estado}: {e}")
    return None

# Lista de códigos dos estados
cod_estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
               'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
               'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

# Dicionário para armazenar a população de cada estado
populacao_estados = {}

# Obtendo a população de cada estado
for cod_estado in cod_estados:
    populacao = obter_populacao_estado(cod_estado)
    if populacao is not None:
        populacao_estados[cod_estado] = populacao

# Função para exibir a lista de populações dos estados
def exibir_lista_populacoes(lista_populacoes):
    print("População de cada estado:")
    for estado, populacao in lista_populacoes:
        print(f"{estado}: {populacao} habitantes")

# Ordenando a lista de populações por ordem alfabética de estado
populacao_ordenada = sorted(populacao_estados.items())

# Exibindo a lista de populações dos estados
exibir_lista_populacoes(populacao_ordenada)
