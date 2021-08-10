from classePessoa import Pessoa

nome = input('Digite o nome :')
idade = int(input('Digite a idade:'))
peso = float(input('Digite o peso :'))
pessoa1 = Pessoa(nome, idade, peso)
print()
print('Antes do aniversário...')
print(pessoa1.__repr__())
print()
print('Depois do aniversário :)')
pessoa1.aniversario()
print(pessoa1.__repr__())
