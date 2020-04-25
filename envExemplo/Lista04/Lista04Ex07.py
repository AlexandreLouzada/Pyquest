# Programa para converter temperatura de Fahrenheit para Celsius
temp_celsius = lambda f: (5/9) * (f - 32)
f = float(input('Entre com a temperatura em Fahrenheit:'))
print(f'A temperatura em Celsius é: {temp_celsius(f):0.2f}')
