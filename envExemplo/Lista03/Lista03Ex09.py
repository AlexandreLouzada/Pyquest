"""
Elabore um programa que contenha três listas de 10 posições A,B e C.
O objetivo do programa é armazenar números nas listas A e B e fazer
com que a lista C receba a soma dos elementos correspondentes de A e B.
Ao final o programa deve exibir no vídeo o conteúdo de C.
"""
A = []
B = []
C = []
tamanho = 3

for indice in range(tamanho):
    A.append(int(input('Digite um número para A: ')))
    B.append(int(input('Digite um número para B: ')))
    C.append(A[indice] + B[indice])

print(f'Tabela A - {A}')
print(f'Tabela B - {B}')
print(f'Tabela C - {C}')
