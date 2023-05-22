class Produto:
    def __init__(self, codigo="", nome="", quantidade=0, valor_unitario=0.0):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

    def inserir(self):
        # Lógica para inserir o produto
        try:
            with open("lista_produto.txt", "a") as arquivo:
                linha = f"{self.codigo};{self.nome};{self.quantidade};{self.valor_unitario}\n"
                arquivo.write(linha)
            return "Produto inserido com sucesso."
        except Exception as e:
            return f"Erro ao inserir produto: {str(e)}"

    def alterar(self):
        # Lógica para alterar o produto
        try:
            with open("lista_produto.txt", "r+") as arquivo:
                linhas = arquivo.readlines()
                arquivo.seek(0)
                for linha in linhas:
                    campos = linha.strip().split(";")
                    if campos[0] == self.codigo:
                        linha = f"{self.codigo};{self.nome};{self.quantidade};{self.valor_unitario}\n"
                    arquivo.write(linha)
                arquivo.truncate()
            return "Produto alterado com sucesso."
        except Exception as e:
            return f"Erro ao alterar produto: {str(e)}"

    def excluir(self):
        # Lógica para excluir o produto
        try:
            with open("lista_produto.txt", "r+") as arquivo:
                linhas = arquivo.readlines()
                arquivo.seek(0)
                for linha in linhas:
                    campos = linha.strip().split(";")
                    if campos[0] != self.codigo:
                        arquivo.write(linha)
                arquivo.truncate()
            return "Produto excluído com sucesso."
        except Exception as e:
            return f"Erro ao excluir produto: {str(e)}"

    def buscar(self, codigo):
        # Lógica para buscar o produto pelo código
        try:
            with open("lista_produto.txt", "r") as arquivo:
                for linha in arquivo:
                    campos = linha.strip().split(";")
                    if campos[0] == codigo:
                        self.nome = campos[1]
                        self.quantidade = int(campos[2])
                        self.valor_unitario = float(campos[3])
                        return "Produto encontrado."
            return "Produto não encontrado."
        except Exception as e:
            return f"Erro ao buscar produto: {str(e)}"
