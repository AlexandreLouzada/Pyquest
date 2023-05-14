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

# Função para adicionar um novo produto à lista
def adicionar_produto():
    novo_produto = Produto(4, "Produto D", 8, 250)
    produtos.append(novo_produto)
    exibir_produtos()

# Função para exibir a lista de produtos na janela
def exibir_produtos():
    # Limpar a janela antes de exibir novamente
    for widget in frame.winfo_children():
        widget.destroy()

    for i, produto in enumerate(produtos):
        label = tk.Label(frame, text=str(produto))
        label.pack()

# Criação da janela principal
root = tk.Tk()
root.title("Lista de Produtos")

# Criação do frame para conter a lista de produtos
frame = tk.Frame(root)
frame.pack()

# Botão para adicionar um novo produto
adicionar_button = tk.Button(root, text="Adicionar Produto", command=adicionar_produto)
adicionar_button.pack()

# Chamada inicial para exibir os produtos
exibir_produtos()

# Início do loop principal da interface gráfica
root.mainloop()

