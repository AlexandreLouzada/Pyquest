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

# Criar um objeto Produto
produto1 = Produto(codigo=123, nome="Arroz", quantidade=50, data_validade="30/06/2023", pais_origem="Tailândia")

# Mostrar detalhes do produto
produto1.mostrardetalhes()

# Adicionar estoque ao produto
produto1.adicionarestoque(25)

# Mostrar detalhes do produto novamente
produto1.mostrardetalhes()

# Verificar a validade do produto
produto1.verificar_validade()

# Verificar taxa de importação do produto
produto1.verificar_taxa_importacao()

