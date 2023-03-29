class Fornecedor:
    def __init__(self, nome, cnpj):
        self._nome = nome
        self._cnpj = cnpj
        self._produto = None

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

    # Getter para o atributo "produto"
    @property
    def produto(self):
        return self._produto

    # Setter para o atributo "produto"
    @produto.setter
    def produto(self, novo_produto):
        self._produto = novo_produto
        if novo_produto:
            novo_produto.fornecedor = self

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


# Cria uma lista vazia de produtos e fornecedores
lista_produtos = []
lista_fornecedores = []

# Cria um produto
produto1 = Produto("001", "Caneta", 100)

# Cria um fornecedor
fornecedor1 = Fornecedor("Fornecedor A", "123456789")

# Adiciona o fornecedor ao produto
produto1.set_fornecedor(fornecedor1)

# Adiciona o produto e o fornecedor às listas
lista_produtos.append(produto1)
lista_fornecedores.append(fornecedor1)

# Exibe as informações dos produtos e fornecedores
print("Produtos:")
for produto in lista_produtos:
    print(f"Produto: {produto.get_nome()} - Código: {produto.get_codigo()} - Quantidade: {produto.get_quantidade()}")
    fornecedor = produto.get_fornecedor()
    print(f"Fornecedor: {fornecedor.get_nome()} - CNPJ: {fornecedor.get_cnpj()}")

print("\nFornecedores:")
for fornecedor in lista_fornecedores:
    print(f"Fornecedor: {fornecedor.get_nome()} - CNPJ: {fornecedor.get_cnpj()}")
    produtos_fornecidos = fornecedor.get_produtos()
    if len(produtos_fornecidos) > 0:
        print("Produtos fornecidos:")
        for produto in produtos_fornecidos:
            print(f"- {produto.get_nome()} - Código: {produto.get_codigo()} - Quantidade: {produto.get_quantidade()}")
    else:
        print("Este fornecedor não fornece nenhum produto.")
