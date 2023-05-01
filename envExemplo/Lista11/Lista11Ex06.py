import pandas as pd
import matplotlib.pyplot as plt

class Investimento:
    def __init__(self, nome, valor, taxa, periodo):
        self.nome = nome
        self.valor = valor
        self.taxa = taxa
        self.periodo = periodo

    def calcular_retorno(self):
        return self.valor * (1 + self.taxa) ** self.periodo

investimentos = {
    'Investimento 1': Investimento('Tesouro Direto', 10000, 0.02, 5),
    'Investimento 2': Investimento('Ações', 5000, 0.05, 3),
    'Investimento 3': Investimento('Poupança', 8000, 0.01, 10),
    'Investimento 4': Investimento('CDB', 15000, 0.03, 7),
}

# Criar um dataframe com os dados dos investimentos
df_investimentos = pd.DataFrame.from_records([i.__dict__ for i in investimentos.values()], index=investimentos.keys())

# Calcular o retorno dos investimentos
df_investimentos['Retorno'] = df_investimentos.apply(lambda row: row.valor * (1 + row.taxa) ** row.periodo, axis=1)

# Plotar um gráfico com o retorno de cada investimento
df_investimentos.plot(kind='bar', y='Retorno', legend=None)
plt.title('Retorno dos Investimentos')
plt.xlabel('Investimentos')
plt.ylabel('Retorno em Reais')
plt.show()
