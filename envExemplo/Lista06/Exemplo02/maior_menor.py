from utilidades import compara

v1 = float(input('Valor 1:'))
v2 = float(input('Valor 2:'))
print()
print('-' * 20)
print('Resultados')
print('-' * 20)
print(f'Maior valor = {compara.maior(v1,v2)}')
print(f'Menor valor = {compara.menor(v1,v2)}')
print('-' * 20)
