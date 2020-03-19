"""
Faça um programa utilizando vetores que leia o nome e a altura de 50 pessoas
e ao final escreva o nome e a altura das pessoas com mais de 1,70 metros.
"""
x=3
listaAltura = []
listaNome = []
for c in range(x):
      listaNome.append(input('Nome: '))
      listaAltura.append(float(input('Altura: ')))
for ind in range(x):
    if listaAltura[ind] > 1.7:
        print(f'Nome:{listaNome[ind]:10} Altura:{listaAltura[ind]:.2f} m')
