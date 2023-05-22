import os
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados do produto:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblcodigo = Label(self.container2, text="Código:", font=self.fonte, width=10)
        self.lblcodigo.pack(side=LEFT)

        self.txtcodigo = Entry(self.container2)
        self.txtcodigo["width"] = 10
        self.txtcodigo["font"] = self.fonte
        self.txtcodigo.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarProduto
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblquantidade = Label(self.container4, text="Quantidade:", font=self.fonte, width=10)
        self.lblquantidade.pack(side=LEFT)

        self.txtquantidade = Entry(self.container4)
        self.txtquantidade["width"] = 25
        self.txtquantidade["font"] = self.fonte
        self.txtquantidade.pack(side=LEFT)

        self.lblvalorunitario = Label(self.container5, text="Valor Unitário:", font=self.fonte, width=10)
        self.lblvalorunitario.pack(side=LEFT)

        self.txtvalorunitario = Entry(self.container5)
        self.txtvalorunitario["width"] = 25
        self.txtvalorunitario["font"] = self.fonte
        self.txtvalorunitario.pack(side=LEFT)

        self.bntInserir = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.bntInserir["command"] = self.inserirProduto
        self.bntInserir.pack(side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarProduto
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirProduto
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserirProduto(self):
        produto = Produto()

        produto.codigo = self.txtcodigo.get()
        produto.nome = self.txtnome.get()
        produto.quantidade = self.txtquantidade.get()
        produto.valor_unitario = self.txtvalorunitario.get()

        self.lblmsg["text"] = produto.inserirProduto()

        self.txtcodigo.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtquantidade.delete(0, END)
        self.txtvalorunitario.delete(0, END)

    def alterarProduto(self):
        produto = Produto()

        produto.codigo = self.txtcodigo.get()
        produto.nome = self.txtnome.get()
        produto.quantidade = self.txtquantidade.get()
        produto.valor_unitario = self.txtvalorunitario.get()

        self.lblmsg["text"] = produto.alterarProduto()

        self.txtcodigo.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtquantidade.delete(0, END)
        self.txtvalorunitario.delete(0, END)

    def excluirProduto(self):
        produto = Produto()

        produto.codigo = self.txtcodigo.get()

        self.lblmsg["text"] = produto.excluirProduto()

        self.txtcodigo.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtquantidade.delete(0, END)
        self.txtvalorunitario.delete(0, END)

    def buscarProduto(self):
        produto = Produto()

        codigo = self.txtcodigo.get()

        self.lblmsg["text"] = produto.buscarProduto(codigo)

        self.txtcodigo.delete(0, END)
        self.txtcodigo.insert(INSERT, produto.codigo)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, produto.nome)

        self.txtquantidade.delete(0, END)
        self.txtquantidade.insert(INSERT, produto.quantidade)

        self.txtvalorunitario.delete(0, END)
        self.txtvalorunitario.insert(INSERT, produto.valor_unitario)


class Produto:
    def __init__(self, codigo="", nome="", quantidade=0, valor_unitario=0.0):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

    def inserirProduto(self):
        # Lógica para inserir o produto
        try:
            with open("lista_produto.txt", "a") as arquivo:
                linha = f"{self.codigo};{self.nome};{self.quantidade};{self.valor_unitario}\n"
                arquivo.write(linha)
            return "Produto inserido com sucesso."
        except Exception as e:
            return f"Erro ao inserir produto: {str(e)}"

    def alterarProduto(self):
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

    def excluirProduto(self):
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

    def buscarProduto(self, codigo):
        # Lógica para buscar o produto pelo código
        try:
            with open("lista_produto.txt", "r") as arquivo:
                for linha in arquivo:
                    campos = linha.strip().split(";")
                    if campos[0] == codigo:
                        self.codigo = campos[0]
                        self.nome = campos[1]
                        self.quantidade = int(campos[2])
                        self.valor_unitario = float(campos[3])
                        return "Produto encontrado."
            return "Produto não encontrado."
        except Exception as e:
            return f"Erro ao buscar produto: {str(e)}"

# Verifica se o arquivo "lista_produto.txt" existe, caso contrário, cria o arquivo
if not os.path.isfile("lista_produto.txt"):
    open("lista_produto.txt", "w").close()

root = Tk()
Application(root)
root.mainloop()
