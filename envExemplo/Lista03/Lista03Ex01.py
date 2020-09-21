"""
Faça um programa utilizando listas que leia o nome e a altura de 50 pessoas
e ao final escreva o nome e a altura das pessoas com mais de 1,70 metros.
"""
x = 3
lista_altura = []
lista_nome = []
for contador in range(x):
    lista_nome.append(input('Nome: '))
    lista_altura.append(float(input('Altura: ')))
for indice in range(x):
    if lista_altura[indice] > 1.7:
        print(f'Nome:{lista_nome[indice]:10} Altura:{lista_altura[indice]:.2f} m')
