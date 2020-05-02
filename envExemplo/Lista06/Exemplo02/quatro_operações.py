from utilidades import calcula

v1 = float(input('Valor 1:'))
v2 = float(input('Valor 2:'))
print()
print('-' * 20)
print('Resultados')
print('-' * 20)
print(f'{v1} + {v2} = {calcula.somar(v1,v2)}')
print(f'{v1} - {v2} = {calcula.subtrair(v1,v2)}')
print(f'{v1} * {v2} = {calcula.multiplicar(v1,v2)}')
print(f'{v1} / {v2} = {calcula.dividir(v1,v2)}')
print('-' * 20)
