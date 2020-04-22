alturas = []
inferior = intermediário = superior = 0
for i in range(4):
    alturas.append(float(input("Insira a altura: ")))
for altura in alturas:
    if altura < 1.60:
        inferior += 1
    elif altura > 1.80:
        superior += 1
    else:
        intermediário += 1
print('-=' * 25)
print(f'Quantidade   de   indivíduos: {len(alturas)}')
print(f'Individuos  abaixo  de  1.60: {inferior}')
print(f'Individuos entre 1.60 e 1.80: {intermediário}')
print(f'Individuos   acima  de  1.80: {superior}')
print('-=' * 25)
