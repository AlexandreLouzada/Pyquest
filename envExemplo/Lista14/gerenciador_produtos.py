from produto import Produto
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

    @staticmethod
    def codigo_existe(arquivo, codigo):
        with open(arquivo, "r") as file:
            for linha in file:
                valores = linha.strip().split(";")
                if len(valores) == 4:
                    codigo_produto, _, _, _ = valores
                    if codigo_produto == codigo:
                        return True
        return False

    @staticmethod
    def incluir_produto(arquivo, produto):
        if GerenciadorProdutos.codigo_existe(arquivo, produto.codigo):
            print("Erro: O código do produto já existe.")
            return

        with open(arquivo, "a") as file:
            linha = f"{produto.codigo};{produto.nome};{produto.quantidade};{produto.valor_unitario}\n"
            file.write(linha)

    @staticmethod
    def consultar_produto(arquivo, codigo):
        with open(arquivo, "r") as file:
            for linha in file:
                valores = linha.strip().split(";")
                if len(valores) == 4:
                    codigo_produto, nome, quantidade, valor_unitario = valores
                    if codigo_produto == codigo:
                        produto = Produto(codigo_produto, nome, int(quantidade), float(valor_unitario))
                        return produto
        return None

    @staticmethod
    def alterar_produto(arquivo, codigo, novo_produto):
        with open(arquivo, "r") as file:
            linhas = file.readlines()

        with open(arquivo, "w") as file:
            for linha in linhas:
                valores = linha.strip().split(";")
                if len(valores) == 4:
                    codigo_produto, _, _, _ = valores
                    if codigo_produto == codigo:
                        file.write(f"{novo_produto.codigo};{novo_produto.nome};{novo_produto.quantidade};{novo_produto.valor_unitario}\n")
                    else:
                        file.write(linha)

    @staticmethod
    def excluir_produto(arquivo, codigo):
        with open(arquivo, "r") as file:
            linhas = file.readlines()

        with open(arquivo, "w") as file:
            for linha in linhas:
                valores = linha.strip().split(";")
                if len(valores) == 4:
                    codigo_produto, _, _, _ = valores
                    if codigo_produto != codigo:
                        file.write(linha)

    @staticmethod
    def listar_produtos(arquivo):
        with open(arquivo, "r") as file:
            for linha in file:
                valores = linha.strip().split(";")
                if len(valores) == 4:
                    codigo, nome, quantidade, valor_unitario = valores
                    produto = Produto(codigo, nome, int(quantidade), float(valor_unitario))
                    print(produto)
