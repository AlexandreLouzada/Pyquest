"""
Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário
para que essa massa se torne menor do que 0.5 gramas. Escreva a massa final, e o tempo.
Observação: o usuário deve digitar a massa inicial.
"""
tempo = 0
massa = float(input('Digite a massa: '))
while massa >= 0.5:
    massa /= 2
    tempo += 50

print(f'Massa: {massa:.2f} Tempo {tempo}')