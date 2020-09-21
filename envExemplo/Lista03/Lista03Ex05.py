"""
Faça um programa utilizando vetores que leia 10 números inteiros
e ao final escreva estes números na ordem crescente e na ordem decrescente.
"""
numero = []
for indice in range(3):
    numero.append(int(input("Digite um número: ")))
numero.sort()
print(f'Os números em ordem crescente ficam   {numero}')
numero.reverse()
print(f'Os números em ordem decrescente ficam {numero}')
