import matplotlib.pyplot as plt

class CampanhaMarketing:
    def __init__(self, canal, investimento, cliques, conversoes):
        self.canal = canal
        self.investimento = investimento
        self.cliques = cliques
        self.conversoes = conversoes
    
    def cpc(self):
        return self.investimento / self.cliques
    
    def taxa_conversao(self):
        return self.conversoes / self.cliques

campanhas = [
    CampanhaMarketing('Facebook Ads', 1000, 15000, 100),
    CampanhaMarketing('Google Ads', 1200, 10000, 200),
    CampanhaMarketing('Email Marketing', 500, 5000, 50),
    CampanhaMarketing('Instagram Ads', 800, 12000, 80),
]

# Criar um gráfico de barras para comparar o CPC das campanhas
canais = [c.canal for c in campanhas]
cpcs = [c.cpc() for c in campanhas]
plt.bar(canais, cpcs)
plt.title('Comparação de CPC por Canal')
plt.xlabel('Canal')
plt.ylabel('CPC')
plt.show()

# Calcular a média de taxa de conversão das campanhas
taxas_conv = [c.taxa_conversao() for c in campanhas]
media_taxa_conv = sum(taxas_conv) / len(campanhas)

print("Média de taxa de conversão das campanhas:", media_taxa_conv)
