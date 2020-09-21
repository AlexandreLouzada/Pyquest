# Programa que calcula a área de um retângulo, círculo ou triângulo

retangulo = lambda lado_a_ret, lado_b_ret: lado_a_ret * lado_b_ret
triangulo = lambda lado_triângulo, altura_triângulo: (lado_triângulo * altura_triângulo) / 2
circulo = lambda raio_circulo: 3.14 * (raio_circulo ** 2)

opcao = -1
while opcao != 0:
    print()
    print('Escolha o objeto que deseja calcular a área')
    print()
    print('1 - Retângulo')
    print('2 - Triângulo')
    print('3 - Círculo')
    print('0 - Sair')
    print()
    opcao = int(input('Entre com o número da opção desejada: '))
    if opcao == 1:
        lado_a = float(input('Entre com um lado do retângulo: '))
        lado_b = float(input('Entre com o outro lado do retângulo: '))
        print(f'\nA área do retâgulo é: {retangulo(lado_a, lado_b):0.2f}')
    elif opcao == 2:
        lado = float(input('Entre com o lado do triângulo: '))
        altura = float(input('Entre com a altura do triângulo: '))
        print(f'\nA área do triângulo é: {triangulo(lado, altura):0.2f}')
    elif opcao == 3:
        raio = float(input('Entre com o raio do cículo:'))
        print(f'\nA área do círculo é: {circulo(raio):0.2f}')
    elif opcao != 0:
        print(f'\n{opcao} não é uma opção válida')
    print()
    print('Fim!')
