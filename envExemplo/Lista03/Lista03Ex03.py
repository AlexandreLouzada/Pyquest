"""
Faça um programa usando vetores que armazene o código, o nome e o telefone
de 100 pessoas. O programa deve permitir que o usuário faça uma consulta dos
dados de uma pessoa a partir de seu código. Esta consulta pode ser repetida
se o usuário desejar, caso contrário, o programa deve ser encerrado.
"""
listcod = []
listnom = []
listtel = []
x= 2
for ind in range(x):
    listcod.append(input('Código: '))
    listnom.append(input('Nome:'))
    listtel.append(input('Telefone:'))

while True:
    codpesq = input('Digite um código para pesquisa : ')
    if codpesq in listcod:
        posição=listcod.index(codpesq)
        print(listnom[posição], listtel[posição])
    else:
        print('Este código não foi encontrado')
    resposta = input('Quer continuar?' )
    if resposta in "Nn":
        break
