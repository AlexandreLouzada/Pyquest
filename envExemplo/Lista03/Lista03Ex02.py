"""
Elabore um programa que leia a matrícula e o salário bruto de 100 empregados.
Os dados devem ser armazenados em vetores. O programa deve descontar 11% do
salário bruto de cada empregado e ao final escrever: a matrícula,
o salário bruto, o desconto e o salário líquido de cada empregado.
"""
listmatricul=[]
listsalbrut= []
listdescont= []
listsalliqui= []
x = 3
for c in range (x):
    listmatricul.append(int(input('Digite a matrícula: ')))
    listsalbrut.append(float(input('Digite o salário: ')))
    listdescont.append((listsalbrut[c] * 11) / 100)
    listsalliqui.append(listsalbrut[c] - listdescont[c])

print('      Matricula  Salario Bruto  Desconto  Salario Liquido')
for c in range (x):
    print(f'{listmatricul[c]:10} {listsalbrut[c]:15.2f} {listdescont[c]:15.2f} {listsalliqui[c]:15.2f}')

