from meu_pacote import Produto

produtos = []

while True:
    print("\nSelecione uma opção:")
    print("1 - Adicionar produto")
    print("2 - Atualizar produto")
    print("3 - Mostrar todos os produtos")
    print("4 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        codigo = int(input("Código do produto: "))
        nome = input("Nome do produto: ")
        quantidade = int(input("Quantidade do produto: "))

        produto = Produto(codigo, nome, quantidade)
        produtos.append(produto)

        print("Produto adicionado com sucesso.")

    elif opcao == 2:
        codigo = int(
            input("Digite o código do produto que deseja atualizar: "))

        for produto in produtos:
            if produto.codigo == codigo:
                print("Digite as novas informações do produto:")
                nome = input("Nome: ")
                quantidade = int(input("Quantidade: "))

                produto.nome = nome
                produto.quantidade = quantidade

                print("Produto atualizado com sucesso.")
                break
        else:
            print("Produto não encontrado.")

    elif opcao == 3:
        for produto in produtos:
            produto.mostrar_detalhes()

    elif opcao == 4:
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")
