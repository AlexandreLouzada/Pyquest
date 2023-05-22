from tkinter import *
import os

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

class ProdutoView:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Produtos")
        self.master.geometry("400x200")

        self.codigo_label = Label(master, text="Código:")
        self.codigo_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)

        self.codigo_entry = Entry(master)
        self.codigo_entry.grid(row=0, column=1, padx=10, pady=10)

        self.nome_label = Label(master, text="Nome:")
        self.nome_label.grid(row=1, column=0, padx=10, pady=10, sticky=E)

        self.nome_entry = Entry(master)
        self.nome_entry.grid(row=1, column=1, padx=10, pady=10)

        self.quantidade_label = Label(master, text="Quantidade:")
        self.quantidade_label.grid(row=2, column=0, padx=10, pady=10, sticky=E)

        self.quantidade_entry = Entry(master)
        self.quantidade_entry.grid(row=2, column=1, padx=10, pady=10)

        self.valor_label = Label(master, text="Valor Unitário:")
        self.valor_label.grid(row=3, column=0, padx=10, pady=10, sticky=E)

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


class Application:
    def __init__(self, master=None):
        self.master = master
        self.produto_view = ProdutoView(master)


if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()
