"""
Faça um programa usando vetores que armazene o código, o nome e o telefone
de 100 pessoas. O programa deve permitir que o usuário faça uma consulta dos
dados de uma pessoa a partir de seu código. Esta consulta pode ser repetida
se o usuário desejar, caso contrário, o programa deve ser encerrado.
"""
codigo = []
nome = []
telefone = []
x = 2
for indice in range(x):
    codigo.append(input('Código: '))
    nome.append(input('Nome:'))
    telefone.append(input('Telefone:'))

while True:
    codpesq = input('Digite um código para pesquisa : ')
    if codpesq in codigo:
        posição = codigo.index(codpesq)
        print(nome[posição], telefone[posição])
    else:
        print('Este código não foi encontrado')
    resposta = input('Quer continuar?' )
    if resposta in "Nn":
        break
