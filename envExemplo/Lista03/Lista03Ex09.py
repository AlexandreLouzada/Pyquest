"""
Elabore um programa que contenha três vetores de 10 posições A,B e C.
O objetivo do programa é armazenar números nos vetores A e B e fazer
com que o vetor C receba a soma dos elementos correspondentes de A e B.
Ao final o programa deve exibir no vídeo o conteúdo de C.
"""
A= []
B= []
C= []
for i in range(4):
    A.append(int(input('Digite um número para A: ')))
    B.append(int(input('Digite um número para B: ')))
    C.append(A[i] + B[i])
print(f'Tabela A - {A}')
print(f'Tabela B - {B}')
print(f'Tabela C - {C}')
