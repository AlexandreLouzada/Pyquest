#ValueError:quando um argumento de uma função tem o tipo certo,
# mas um valor inadequado.
#TypeError:quando é passado um objeto de um tipo diferente do
# tipo que a função espera como argumento.
# KeyboardInterrupt: quando o usuário pressiona a tecla de
# interrupção (Ctrl-C ou Delete ).
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO:digite um número inteiro\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário não digitou o número.\033[m')
            return 0
        else:
            return n
def linha(tam=42):
    return '-' * tam
def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
