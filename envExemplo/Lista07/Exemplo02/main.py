from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

a = PessoaFisica('111.222.333-44', nome='Alfredo', idade=22)

print(a.getcpf())
print(a.getnome())
print(a.getidade())

b = PessoaJuridica('64.614.527/0001-99', nome='Empresa X', idade=22)

print(b.getcnpj())
print(b.getnome())
print(b.getidade())
