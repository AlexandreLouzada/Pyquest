"""
Um banco concederá um crédito especial aos seus clientes, variável com o saldo médio
no último ano. Faça um algoritmo que leia o saldo médio de um cliente e calcule o
valor do crédito de acordo com a tabela abaixo. Mostre uma mensagem informando o
saldo médio e o valor do crédito.

Saldo médio	    Percentual
de 0 a 200	    nenhum crédito
de 201 a 400	20% do valor do saldo médio
de 401 a 600	30% do valor do saldo médio
acima de 601	40% do valor do saldo médio
"""

saldo_medio= float(input('Informe seu saldo medio:'))
if saldo_medio < 200:
    print('nenhum credito foi concedido')
elif saldo_medio >= 200 and saldo_medio <= 400:
    percent= saldo_medio * 20/100
elif saldo_medio > 400 and saldo_medio <= 600:
    percent= saldo_medio * 30/100
else:
    percent= saldo_medio * 40/100
print(f'Seu saldo médio é de {saldo_medio:.2f}')
print(f'O valor de credito é de {percent:.2f}')
