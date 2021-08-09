"""
Fazer um algoritmo para calcular a contribuição ao INSS, IR e a associação
de funcionários a partir do salário bruto, que é dado de entrada. As taxas
sobre o salário bruto são as seguintes:
•	INSS - 10%
•	IR - 25%
•	Sindicato - 2 %
O programa deve imprimir as contribuições e o valor do salário líquido.
"""
salario_bruto = float(input('Informe seu salário:'))
inss= salario_bruto * 10/100
ir= salario_bruto * 25/100
sindicato = salario_bruto * 2/100
salario_liquido= salario_bruto - (inss + ir + sindicato)
print(f'O desconto do INSS é de R${inss:.2f}')
print(f'O desconto do IR é de R${ir:.2f}')
print(f'O desconto do sindicato é de R${sindicato:.2f}')
print(f'O seu salario liquido é de R${salario_liquido:.2f}')