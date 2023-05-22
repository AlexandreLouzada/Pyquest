from produto import Produto
from tkinter import *

class ProdutoView:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Produtos")
        self.master.geometry("400x300")

        self.codigo_label = Label(master, text="Código:")
        self.codigo_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.codigo_entry = Entry(master)
        self.codigo_entry.grid(row=0, column=1, padx=10, pady=10)

        self.nome_label = Label(master, text="Nome:")
        self.nome_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.nome_entry = Entry(master)
        self.nome_entry.grid(row=1, column=1, padx=10, pady=10)

        self.quantidade_label = Label(master, text="Quantidade:")
        self.quantidade_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.quantidade_entry = Entry(master)
        self.quantidade_entry.grid(row=2, column=1, padx=10, pady=10)

        self.valor_label = Label(master, text="Valor Unitário:")
        self.valor_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.valor_entry = Entry(master)
        self.valor_entry.grid(row=3, column=1, padx=10, pady=10)

        self.btn_inserir = Button(master, text="Inserir", command=self.inserir_produto)
        self.btn_inserir.grid(row=4, column=0, padx=10, pady=10)

        self.btn_alterar = Button(master, text="Alterar", command=self.alterar_produto)
        self.btn_alterar.grid(row=4, column=1, padx=10, pady=10)

        self.btn_excluir = Button(master, text="Excluir", command=self.excluir_produto)
        self.btn_excluir.grid(row=5, column=0, padx=10, pady=10)

        self.btn_buscar = Button(master, text="Buscar", command=self.buscar_produto)
        self.btn_buscar.grid(row=5, column=1, padx=10, pady=10)

        self.status_label = Label(master, text="")
        self.status_label.grid(row=6, columnspan=2, padx=10, pady=10)

    def get_codigo(self):
        return self.codigo_entry.get()

    def get_nome(self):
        return self.nome_entry.get()

    def get_quantidade(self):
        return int(self.quantidade_entry.get())

    def get_valor_unitario(self):
        return float(self.valor_entry.get())

    def set_status(self, status):
        self.status_label.config(text=status)

    def limpar_campos(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.quantidade_entry.delete(0, END)
        self.valor_entry.delete(0, END)

    def inserir_produto(self):
        codigo = self.get_codigo()
        nome = self.get_nome()
        quantidade = self.get_quantidade()
        valor_unitario = self.get_valor_unitario()

        produto = Produto(codigo, nome, quantidade, valor_unitario)
        resultado = produto.inserir()

        self.set_status(resultado)
        self.limpar_campos()

    def alterar_produto(self):
        codigo = self.get_codigo()
        nome = self.get_nome()
        quantidade = self.get_quantidade()
        valor_unitario = self.get_valor_unitario()

        produto = Produto(codigo, nome, quantidade, valor_unitario)
        resultado = produto.alterar()

        self.set_status(resultado)
        self.limpar_campos()

    def excluir_produto(self):
        codigo = self.get_codigo()

        produto = Produto(codigo)
        resultado = produto.excluir()

        self.set_status(resultado)
        self.limpar_campos()

    def buscar_produto(self):
        codigo = self.get_codigo()

        produto = Produto()
        resultado = produto.buscar(codigo)

        if resultado == "Produto encontrado.":
            self.codigo_entry.insert(END, produto.codigo)
            self.nome_entry.insert(END, produto.nome)
            self.quantidade_entry.insert(END, produto.quantidade)
            self.valor_entry.insert(END, produto.valor_unitario)

        self.set_status(resultado)
