from tkinter import Tk
from produto_view import ProdutoView
from produto import Produto


class Application:
    def __init__(self, master=None):
        self.master = master
        self.produto_view = ProdutoView(master)


if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()
    
