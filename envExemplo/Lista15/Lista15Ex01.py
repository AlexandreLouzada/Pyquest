# Dicionário para armazenar a população de cada estado
populacao_estados = {}

# Obtendo a população de cada estado
while True:
    estado = input("Digite o nome do estado (ou 'sair' para encerrar): ")
    if estado.lower() == 'sair':
        break
    populacao = int(input("Digite a população do estado: "))
    populacao_estados[estado] = populacao

# Exibindo os resultados
print("\nPopulação de cada estado:")
for estado, populacao in populacao_estados.items():
    print(f"{estado}: {populacao} habitantes")
