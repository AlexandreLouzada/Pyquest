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

    # Getter para o atributo "produtos"
    @property
    def produtos(self):
        return self._produtos

    # Método para adicionar um produto a lista de produtos fornecidos pelo fornecedor
    def adicionar_produto(self, produto):
        self._produtos.append(produto)
        if produto not in self.produtos:
            produto.adicionar_fornecedor(self)

class Produto:
    def __init__(self, codigo, nome, quantidade):
        self._codigo = codigo
        self._nome = nome
        self._quantidade = quantidade
        self._fornecedores = []

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

    # Getter para o atributo "fornecedores"
    @property
    def fornecedores(self):
        return self._fornecedores

    # Método para adicionar um fornecedor à lista de fornecedores do produto
    def adicionar_fornecedor(self, fornecedor):
        self._fornecedores.append(fornecedor)
        if self not in fornecedor.produtos:
            fornecedor.adicionar_produto(self)

# Cria um produto
produto1 = Produto("001", "Caneta", 100)

# Cria um fornecedor
fornecedor1 = Fornecedor("Fornecedor A", "123456789")

# Adiciona o fornecedor ao produto
produto1.adicionar_fornecedor(fornecedor1)

# Adiciona o produto ao fornecedor
fornecedor1.adicionar_produto(produto1)

# Exibe as informações do produto e do fornecedor
print(f"Produto: {produto1.nome} - Código: {produto1.codigo} - Quantidade: {produto1.quantidade}")
print(f"Fornecedor: {fornecedor1.nome} - CNPJ: {fornecedor1.cnpj}")
print("Produtos fornecidos:")
for produto in fornecedor1.produtos:
    print(f"- {produto.nome}")
    

