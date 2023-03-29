"""um exemplo de programa em Python que usa programação orientada a objetos para criar uma classe "Produto" com os atributos "código", "nome" e "quantidade". associe essa classe a uma outra classe de nome "Fornecedor". Cada produto pode ter um fornecedor mas cada fornecedor pode fornecer vários produtos."""

class Fornecedor:
    def __init__(self, nome, cnpj):
        self._nome = nome
        self._cnpj = cnpj
        self._produtos = []

    # Getter para o atributo "nome"
    @property
    def nome(self):
        return self._nome

    # Setter para o atributo "nome"
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    # Getter para o atributo "cnpj"
    @property
    def cnpj(self):
        return self._cnpj

    # Setter para o atributo "cnpj"
    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self._cnpj = novo_cnpj

    # Método para adicionar um produto ao fornecedor
    def adicionar_produto(self, produto):
        self._produtos.append(produto)

    # Método para listar os produtos do fornecedor
    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome)

class Produto:
    def __init__(self, codigo, nome, quantidade, fornecedor=None):
        self._codigo = codigo
        self._nome = nome
        self._quantidade = quantidade
        self._fornecedor = fornecedor

    # Getter para o atributo "codigo"
    @property
    def codigo(self):
        return self._codigo

    # Setter para o atributo "codigo"
    @codigo.setter
    def codigo(self, novo_codigo):
        self._codigo = novo_codigo

    # Getter para o atributo "nome"
    @property
    def nome(self):
        return self._nome

    # Setter para o atributo "nome"
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    # Getter para o atributo "quantidade"
    @property
    def quantidade(self):
        return self._quantidade

    # Setter para o atributo "quantidade"
    @quantidade.setter
    def quantidade(self, nova_quantidade):
        self._quantidade = nova_quantidade

    # Getter para o atributo "fornecedor"
    @property
    def fornecedor(self):
        return self._fornecedor

    # Setter para o atributo "fornecedor"
    @fornecedor.setter
    def fornecedor(self, novo_fornecedor):
        self._fornecedor = novo_fornecedor
        if novo_fornecedor:
            novo_fornecedor.adicionar_produto(self)

# Cria um produto
produto1 = Produto("001", "Caneta", 100)

# Cria um fornecedor
fornecedor1 = Fornecedor("Fornecedor A", "123456789")

# Adiciona o fornecedor ao produto
produto1.adicionar_fornecedor(fornecedor1)

# Exibe as informações do produto e do fornecedor
print(f"Produto: {produto1.nome} - Código: {produto1.codigo} - Quantidade: {produto1.quantidade}")
print(f"Fornecedor: {produto1.fornecedor.nome} - CNPJ: {produto1.fornecedor.cnpj}")
