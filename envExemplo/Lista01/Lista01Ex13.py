"""
Faça um programa que leia três números diferentes e informe o maior deles.
Se os números digitados não forem diferentes o programa deve gerar a mensagem:
“Os valores digitados não são diferentes”.
"""
num01 = int(input('Digite um valor:'))
num02 = int(input('Digite um valor:'))
num03 = int(input('Digite um valor:'))
if num01 == num02 == num03:
    print('os numeros são iguais')
elif num01 > num02 and num01 > num03:
    maior = num01
elif num02 > num01 and num02 > num03:
    maior = num02
elif num03 > num01 and num03 > num02:
    maior = num03
print('Maior número: {}'.format(maior))
