"""
Elabore um programa que leia o salário de um empregado e com base na tabela
 abaixo calcule e informe sua gratificação e seu salário líquido.

FAIXA SALARIAL                  	GRATIFICAÇÃO
Menor que 2000                          5%
De 2000 a 2500                      	10%
Maior que 2500 e menor ou igual a 3000	15%
Maior que 3000                      	20%
"""
salario_bruto = float(input('digite o seu salario:'))
if salario_bruto < 2000:
    gratificaçao = salario_bruto * 5/100
elif salario_bruto >= 2000 and salario_bruto <= 2500:
    gratificaçao = salario_bruto * 10/100
elif salario_bruto > 2500 and salario_bruto <= 3000:
    gratificaçao = salario_bruto * 15/100
else:
    gratificaçao = salario_bruto * 20/100
salario_liquido = salario_bruto + gratificaçao
print('seu salario liquido é de R${}'.format(salario_liquido))
print('Sua gratificação foi de R${}'.format(gratificaçao))
