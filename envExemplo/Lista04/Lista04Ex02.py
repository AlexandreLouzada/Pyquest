def testa_recursão(valor):
    if valor > 0:
        result = valor + testa_recursão(valor-1)
        print(result)
    else:
        result = 0
    return result


print('\n\nResultado da recursão')
testa_recursão(3)
