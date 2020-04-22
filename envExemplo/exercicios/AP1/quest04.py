valor1 = float(input('Digite o primeiro número: '))
valor2 = float(input('Digite o segundo  número: '))
if valor1 > valor2:
    print(f'Maior número {valor1}')
elif valor2 > valor1:
    print(f'Maior número {valor2}')
else:
    print(f'Os valores são iguais')
