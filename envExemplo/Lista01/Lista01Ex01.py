"""
Escreva um programa que calcule a quantidade de litros de combustível gastos em uma viagem,
considerando que o automóvel consome 1 litro a cada 12 Km. Para obter o consumo, o usuário
deve fornecer o tempo gasto na viagem e a velocidade média durante a mesma. Desta forma,
será possível obter a distância percorrida com a seguinte fórmula DISTÂNCIA = TEMPO * VELOCIDADE.
Tendo o valor da distância, basta calcular a quantidade de litros com a fórmula
LITROS_USADOS = DISTÂNCIA/12. Deve ser fornecido como resposta: a velocidade média, o tempo gasto
na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.
"""
tempo = float(input('digite o tempo gasto:'))
velocidade = int(input('digite a velocidade media:'))
distancia = tempo * velocidade
litros_usados= distancia/12
print('o tempo gasto foi de {:.2f} horas'.format(tempo))
print('A velocidade media foi de {} km/h'.format(velocidade))
print('A distancia percorrida foi de {} km'.format(distancia))
print('A quantidade de combustivel foi de {:.2f} Litros'.format(litros_usados))
