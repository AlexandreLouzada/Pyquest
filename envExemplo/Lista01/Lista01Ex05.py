"""
Construir um programa que leia o salário bruto e o sexo de um funcionário.
Se o sexo for “M” (masculino), calcular, armazenar e imprimir um desconto
de 5% e o salário líquido, caso contrário, calcular, armazenar e imprimir
um desconto de 3% e o salário líquido.
"""
salario= float(input('Digite seu salário bruto:'))
sexo= input('Se você for do sexo masculino digite "m", se for do sexo feminino digite "f": ')
sexo = sexo.upper()
if sexo == 'M':
    saliq= salario * 5/100
elif sexo == 'F':
    saliq= salario * 3/100
print('Seu salario liquido é de {}'.format(saliq))
