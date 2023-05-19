from produto import Produto
from gerenciador_produtos import GerenciadorProdutos


def exibir_menu():
    print("1. Incluir produto")
    print("2. Consultar produto")
    print("3. Alterar produto")
    print("4. Excluir produto")
    print("5. Listar produtos")
    print("6. Sair")


def executar_menu():
    arquivo = "lista_produtos.txt"
    gerenciador = GerenciadorProdutos(arquivo)

    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            codigo = input("Digite o código do produto: ")
            if GerenciadorProdutos.codigo_existe(arquivo, codigo):
                print("Erro: O código do produto já existe.")
                continue
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade do produto: "))
            valor_unitario = float(input("Digite o valor unitário do produto: "))
            produto = Produto(codigo, nome, quantidade, valor_unitario)
            gerenciador.incluir_produto(arquivo, produto)
            print("Produto incluído com sucesso!")

        elif opcao == "2":
            codigo = input("Digite o código do produto: ")
            produto = gerenciador.consultar_produto(arquivo, codigo)
            if produto:
                print(produto)
            else:
                print("Produto não encontrado.")

        elif opcao == "3":
            codigo = input("Digite o código do produto a ser alterado: ")
            novo_codigo = input("Digite o novo código do produto: ")
            novo_nome = input("Digite o novo nome do produto: ")
            nova_quantidade = int(input("Digite a nova quantidade do produto: "))
            novo_valor_unitario = float(input("Digite o novo valor unitário do produto: "))
            novo_produto = Produto(novo_codigo, novo_nome, nova_quantidade, novo_valor_unitario)
            gerenciador.alterar_produto(arquivo, codigo, novo_produto)
            print("Produto alterado com sucesso!")

        elif opcao == "4":
            codigo = input("Digite o código do produto a ser excluído: ")
            gerenciador.excluir_produto(arquivo, codigo)
            print("Produto excluído com sucesso!")

        elif opcao == "5":
            gerenciador.listar_produtos(arquivo)

        elif opcao == "6":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Digite novamente.")


if __name__ == "__main__":
    executar_menu()

