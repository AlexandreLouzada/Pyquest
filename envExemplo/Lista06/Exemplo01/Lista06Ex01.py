from calcula import *
valor1 = float(input('Valor 1:'))
valor2 = float(input('Valor 2:'))
print()
print('-' * 20)
print('Resultados')
print('-' * 20)
print(f'{valor1} + {valor2} = {somar(valor1,valor2)}')
print(f'{valor1} - {valor2} = {subtrair(valor1,valor2)}')
print(f'{valor1} * {valor2} = {multiplicar(valor1,valor2)}')
print(f'{valor1} / {valor2} = {dividir(valor1,valor2)}')
print('-' * 20)
