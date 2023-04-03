from meu_pacote import Produto

produto1 = Produto(1, "Caneta", 10)
produto2 = Produto(2, "Lápis", 5)

produto1.mostrar_detalhes()
produto1.adicionar_estoque(5)
produto1.mostrar_detalhes()

produto2.mostrar_detalhes()
produto2.adicionar_estoque(3)
produto2.mostrar_detalhes()
