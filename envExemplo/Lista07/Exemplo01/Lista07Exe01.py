from minhaclasse import Pessoa

p1 = Pessoa()
p2 = Pessoa()
p1.nome = 'Pedro'
p2.nome = 'Maria'
p1.idade = 19
p2.idade = p1.idade + 3
p1.aniversario()
p1.peso = 120.8
p2.peso = p1.peso / 2
print(p1)
print(p2)
