"""
Elabore um programa utilizando vetores para armazenar 10 números
e ao final escreva a quantidade de números negativos, positivos e nulos.
"""
numero = []
negativo = positivo = zero = 0

for n in range(10):
    numero.append(int(input('Digite um número: ')))
    if numero[n] < 0:
        negativo += 1
    elif numero[n] == 0:
        zero += 1
    else:
        positivo += 1

print(f'A quantidade de números negativos da lista são {negativo}')
print(f'A quantidade de números positivos na lista são {positivo}')
print(f'A quantidade de números nulos na lista são {zero}')
