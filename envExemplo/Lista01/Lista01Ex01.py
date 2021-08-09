"""
Escreva um programa que calcule a quantidade de litros de combustível gastos em uma viagem,
considerando que o automóvel consome 1 litro a cada 12 Km. Para obter o consumo, o usuário
deve fornecer o tempo gasto na viagem e a velocidade média durante a mesma. Desta forma,
será possível obter a distância percorrida com a seguinte fórmula DISTÂNCIA = TEMPO * VELOCIDADE.
Tendo o valor da distância, basta calcular a quantidade de litros com a fórmula
LITROS_USADOS = DISTÂNCIA/12. Deve ser fornecido como resposta: a velocidade média, o tempo gasto
na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.
"""
tempo = float(input('Digite o tempo gasto (HH:MM):'))
velocidade = int(input('digite a velocidade media:'))
distancia = tempo * velocidade
litros_usados = distancia / 12

print(f'O tempo gasto foi de {tempo:.2f} horas')
print(f'A velocidade media foi de {velocidade} km/h')
print(f'A distancia percorrida foi de {distancia} km')
print(f'A quantidade de combustivel foi de {litros_usados:.2f} Litros')