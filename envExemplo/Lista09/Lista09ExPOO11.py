class ProdutoPerecivel:
    def __init__(self, data_validade):
        self.data_validade = data_validade

    def verificar_validade(self):
        print(f"Verificando validade do produto com data de validade {self.data_validade}")

class ProdutoImportado:
    def __init__(self, pais_origem):
        self.pais_origem = pais_origem

    def verificar_taxa_importacao(self):
        print(f"Verificando taxa de importação do produto importado de {self.pais_origem}")

class Produto(ProdutoPerecivel, ProdutoImportado):
    def __init__(self, codigo, nome, quantidade, data_validade, pais_origem):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        ProdutoPerecivel.__init__(self, data_validade)
        ProdutoImportado.__init__(self, pais_origem)

    def mostrardetalhes(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Data de validade: {self.data_validade}")
        print(f"País de origem: {self.pais_origem}")

    def adicionarestoque(self, quantidade):
        self.quantidade += quantidade

