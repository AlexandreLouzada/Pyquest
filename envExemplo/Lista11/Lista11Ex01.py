import numpy as np

# Definindo uma lista de números
numeros = [1, 2, 3, 4, 5]

# Convertendo a lista para um array NumPy
array_numeros = np.array(numeros)

# Calculando a média dos números usando a função mean do NumPy
media = np.mean(array_numeros)

# Imprimindo o resultado
print("A média é:", media)
