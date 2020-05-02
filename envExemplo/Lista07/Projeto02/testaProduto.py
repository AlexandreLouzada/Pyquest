from classeProduto import Produto

p = Produto()
fabricante = input('Digite o fabricante:')
p.setFabricante(fabricante)
preço = float(input('Digite o preço:'))
p.setPreço(preço)
print()
print(f'Nome do fabricante: {p.getFabricante()}')
print(f'Preço obtido......: {p.getPreço()}')
