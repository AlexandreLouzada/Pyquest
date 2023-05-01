import numpy as np
from scipy.stats import norm

vendas = [20, 30, 25, 40, 35, 50, 45, 60, 55, 70, 65, 80]

media = np.mean(vendas)
desvio_padrao = np.std(vendas)

# calcular a probabilidade de uma venda ser menor que 50
probabilidade = norm.cdf(50, media, desvio_padrao)

# calcular a demanda esperada para o próximo mês
# supondo que a loja vende 1000 unidades por mês
demanda_esperada = probabilidade * 1000 

print("A média das vendas é:", media)
print("O desvio padrão das vendas é:", desvio_padrao)
print("A demanda esperada para o próximo mês é:", demanda_esperada)

