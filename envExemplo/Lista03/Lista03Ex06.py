"""
Elabore um programa utilizando vetores para armazenar 10 números
e ao final escreva a quantidade de números negativos, positivos e nulos.
"""
listnum = []
neg = pos = nul= 0
for n in range(10):
    listnum.append(int(input('Digite um número: ')))
    if listnum[n] < 0:
        neg += 1
    elif listnum[n] == 0:
        nul += 1
    else:
        pos += 1
print(f'A quantidade de números negativos da lista são {neg}')
print(f'A quantidade de números positivos na lista são {pos}')
print(f'A quantidade de números nulos na lista são {nul}')
