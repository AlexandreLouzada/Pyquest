# Um exemplo de calculadora simples utilizando funções

def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def multiplicacao(num1, num2):
    return num1 * num2


def divisao(num1, num2):
    return num1 / num2


# Programa principal
opcao = 1
while opcao:
    print('-' * 20)
    print('0. Sair')
    print('1. Somar')
    print('2. Subtrair')
    print('3. Multiplicação')
    print('4. Divisão ')
    print('-' * 20)
    opcao = int(input('Opção: '))
    if opcao == 0:
        break
    print('-' * 20)
    valor1 = float(input('Primeiro número: '))
    valor2 = float(input('Segundo número : '))
    print('-' * 20)
    if opcao == 1:
        print(f'{valor1} + {valor2} = {soma(valor1, valor2)}')
    if opcao == 2:
        print(f'{valor1} - {valor2} = {subtracao(valor1, valor2)}')
    if opcao == 3:
        print(f'{valor1} * {valor2} = {multiplicacao(valor1, valor2)}')
    if opcao == 4:
        print(f'{valor1} / {valor2} = {divisao(valor1, valor2)}')
