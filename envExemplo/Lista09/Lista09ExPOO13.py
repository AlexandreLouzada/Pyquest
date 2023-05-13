class Produto:
    def __init__(self, codigo, nome, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade

    def mostrar_detalhes(self):
        print("Detalhes do Produto:")
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade

    def __str__(self):
        return f"Código: {self.codigo}\nNome: {self.nome}\nQuantidade: {self.quantidade}"

    def __eq__(self, other):
        if isinstance(other, Produto):
            return self.codigo == other.codigo
        return False

    def __lt__(self, other):
        if isinstance(other, Produto):
            return self.quantidade < other.quantidade
        raise TypeError("Incompatível com a comparação")

    def __len__(self):
        return self.quantidade

    def __repr__(self):
        return f"Produto(codigo={self.codigo}, nome='{self.nome}', quantidade={self.quantidade})"

    def __getitem__(self, index):
        if index == 'codigo':
            return self.codigo
        elif index == 'nome':
            return self.nome
        elif index == 'quantidade':
            return self.quantidade
        else:
            raise KeyError(f"Chave inválida: {index}")

    def __setitem__(self, index, value):
        if index == 'codigo':
            self.codigo = value
        elif index == 'nome':
            self.nome = value
        elif index == 'quantidade':
            self.quantidade = value
        else:
            raise KeyError(f"Chave inválida: {index}")

    def __iter__(self):
        yield 'codigo', self.codigo
        yield 'nome', self.nome
        yield 'quantidade', self.quantidade


# Exemplo de uso dos novos métodos
produto = Produto(1, "Camiseta", 10)

# Exemplo de __repr__
print(repr(produto))  # Retorna uma representação do objeto em formato de string

# Exemplo de __getitem__
print(produto['codigo'])  # Acessa o atributo código
print(produto['nome'])    # Acessa o atributo nome
print(produto['quantidade'])  # Acessa o atributo quantidade
# print(produto['preco'])  # Lançará uma exceção KeyError, pois a chave 'preco' é inválida

# Exemplo de __setitem__
produto['codigo'] = 2     # Atualiza o valor do atributo código
produto['nome'] = 'Calça'  # Atualiza o valor do atributo nome
produto['quantidade'] = 5   # Atualiza o valor do atributo quantidade

# Exemplo de __iter__
for chave, valor in produto:
    print(chave, "=", valor)
