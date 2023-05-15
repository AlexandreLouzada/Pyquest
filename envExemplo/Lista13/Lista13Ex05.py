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

    def incluir_produto(self, produto):
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


# Exemplo de uso do sistema
gerenciador = GerenciadorProdutos("lista_produtos.txt")

# Incluindo um novo produto
novo_produto = Produto("001", "Produto 1", 10, 9.99)
gerenciador.incluir_produto(novo_produto)

# Consultando um produto pelo código
produto_consultado = gerenciador.consultar_produto("001")
if produto_consultado:
    print("Produto encontrado:")
    print(produto_consultado)
else:
    print("Produto não encontrado.")

# Alterando um produto pelo código
novo_produto = Produto("001", "Produto 1 Modificado", 20, 19.99)
gerenciador.alterar_produto("001", novo_produto)

# Excluindo um produto pelo código
gerenciador.excluir_produto("001")

# Listando todos os produtos
gerenciador.listar_produtos()

