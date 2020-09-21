"""
Um programa que verifica de um valor inteiro
é positivo, negativo ou igual a zero
"""


def verifica_valor(valor):
    if valor > 0:
        return f'O número {valor} é positivo.'
    elif valor < 0:
        return f'O número {valor} é negativo.'
    else:
        return f'O número é igual a zero.'


# Programa principal
print('')
print('-' * 30)
numero = int(input('Digite um valor inteiro: '))
print(verifica_valor(numero))
print('-' * 30)
