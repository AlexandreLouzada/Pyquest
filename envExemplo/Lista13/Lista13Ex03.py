import tkinter as tk

class Produto:
    def __init__(self, codigo, nome, quantidade, valor_unitario):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

    def __repr__(self):
        return f"Produto({self.codigo}, '{self.nome}', {self.quantidade}, {self.valor_unitario})"

# Lista de produtos
produtos = [
    Produto(3, "Produto C", 15, 300),
    Produto(1, "Produto A", 10, 100),
    Produto(2, "Produto B", 5, 200),
]

# Função para exibir a lista de produtos na janela
def exibir_produtos():
    for i, produto in enumerate(produtos):
        label = tk.Label(root, text=str(produto))
        label.pack()

# Criação da janela principal
root = tk.Tk()
root.title("Lista de Produtos")

# Chamada da função para exibir os produtos
exibir_produtos()

# Início do loop principal da interface gráfica
root.mainloop()

