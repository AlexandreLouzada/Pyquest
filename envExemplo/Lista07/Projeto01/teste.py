from classePessoa import Pessoa

nome = input('Digite o nome :')
idade = int(input('Digite a idade:'))
peso = float(input('Digite o peso :'))
p1 = Pessoa(nome, idade, peso)
print()
print('Antes do aniversário...')
print(p1.__repr__())
print()
print('Depois do aniversário :)')
p1.aniversario()
print(p1.__repr__())
