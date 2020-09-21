"""
Elabore um programa que leia a matrícula e o salário bruto de 100 empregados.
Os dados devem ser armazenados em vetores. O programa deve descontar 11% do
salário bruto de cada empregado e ao final escrever: a matrícula,
o salário bruto, o desconto e o salário líquido de cada empregado.
"""
matricula =[]
salario_bruto = []
desconto = []
salario_liquido = []
x = 3
for indice in range(x):
    matricula.append(int(input('Digite a matrícula: ')))
    salario_bruto.append(float(input('Digite o salário: ')))
    desconto.append((salario_bruto[indice] * 11) / 100)
    salario_liquido.append(salario_bruto[indice] - desconto[indice])

print('      Matricula  Salario Bruto  Desconto  Salario Liquido')
for indice in range(x):
    print(f'{matricula[indice]:10} {salario_bruto[indice]:11.2f} {desconto[indice]:11.2f} {salario_liquido[indice]:15.2f}')

