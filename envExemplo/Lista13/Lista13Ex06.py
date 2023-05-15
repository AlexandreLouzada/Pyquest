class Produto:
    def __init__(self, codigo, nome, quantidade, valor_unitario):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

    def __str__(self):
        return f"Código: {self.codigo}\nNome: {self.nome}\nQuantidade: {self.quantidade}\nValor Unitário: {self.valor_unitario}\n"


class GerenciadorProdutos:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.criar_arquivo()

    def criar_arquivo(self):
        try:
            with open(self.arquivo, "x"):
                pass
        except FileExistsError:
            pass


    def codigo_existe(self, codigo):
        with open(self.arquivo, "r") as file:
            for linha in file:
                valores = linha.strip().split(";")
                if len(valores) == 4:
                    codigo_produto, _, _, _ = valores
                    if codigo_produto == codigo:
                        return True
        return False

    def incluir_produto(self, produto):
        if self.codigo_existe(produto.codigo):
            print("Erro: O código do produto já existe.")
            return

        with open(self.arquivo, "a") as file:
            linha = f"{produto.codigo};{produto.nome};{produto.quantidade};{produto.valor_unitario}\n"
            file.write(linha)

 
    def consultar_produto(self, codigo):
        with open(self.arquivo, "r") as file:
            for linha in file:
                valores = linha.strip().split(";")
                if len(valores) == 4:
                    codigo_produto, nome, quantidade, valor_unitario = valores
                    if codigo_produto == codigo:
                        produto = Produto(codigo_produto, nome, int(quantidade), float(valor_unitario))
                        return produto
        return None

    def alterar_produto(self, codigo, novo_produto):
        with open(self.arquivo, "r") as file:
            linhas = file.readlines()

        with open(self.arquivo, "w") as file:
            for linha in linhas:
                valores = linha.strip().split(";")
                if len(valores) == 4:
                    codigo_produto, _, _, _ = valores
                    if codigo_produto == codigo:
                        file.write(f"{novo_produto.codigo};{novo_produto.nome};{novo_produto.quantidade};{novo_produto.valor_unitario}\n")
                    else:
                        file.write(linha)

    def excluir_produto(self, codigo):
        with open(self.arquivo, "r") as file:
            linhas = file.readlines()

        with open(self.arquivo, "w") as file:
            for linha in linhas:
                valores = linha.strip().split(";")
                if len(valores) == 4:
                    codigo_produto, _, _, _ = valores
                    if codigo_produto != codigo:
                        file.write(linha)

    def listar_produtos(self):
        with open(self.arquivo, "r") as file:
            for linha in file:
                valores = linha.strip().split(";")
                if len(valores) == 4:
                    codigo, nome, quantidade, valor_unitario = valores
                    produto = Produto(codigo, nome, int(quantidade), float(valor_unitario))
                    print(produto)


def exibir_menu():
    print("1. Incluir produto")
    print("2. Consultar produto")
    print("3. Alterar produto")
    print("4. Excluir produto")
    print("5. Listar produtos")
    print("6. Sair")


gerenciador = GerenciadorProdutos("lista_produtos.txt")

while True:
    exibir_menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        codigo = input("Digite o código do produto: ")
        if gerenciador.codigo_existe(codigo):
            print("Erro: O código do produto já existe.")
            continue
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade do produto: "))
        valor_unitario = float(input("Digite o valor unitário do produto: "))
        produto = Produto(codigo, nome, quantidade, valor_unitario)
        gerenciador.incluir_produto(produto)
        print("Produto incluído com sucesso!")

    elif opcao == "2":
        codigo = input("Digite o código do produto: ")
        produto = gerenciador.consultar_produto(codigo)
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
        gerenciador.alterar_produto(codigo, novo_produto)
        print("Produto alterado com sucesso!")

    elif opcao == "4":
        codigo = input("Digite o código do produto a ser excluído: ")
        gerenciador.excluir_produto(codigo)
        print("Produto excluído com sucesso!")

    elif opcao == "5":
        gerenciador.listar_produtos()

    elif opcao == "6":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Digite novamente.")

