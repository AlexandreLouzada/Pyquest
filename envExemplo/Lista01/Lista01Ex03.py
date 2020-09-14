"""
Construir um programa que leia as 2 notas de um aluno e que calcule,
armazene e imprima a média. Se a média for maior ou igual a 7, imprimir
“Aprovado”, caso contrário, realizar a leitura de uma terceira nota,
que terá peso 2 e calcular, armazenar e imprimir uma nova média.
Se a nova média for maior ou igual a 6, imprimir “Aprovado”, caso contrário,
imprimir “Reprovado”.
"""
nota1 = float(input('digite sua primeira nota:'))
nota2 = float(input('digite sua segunda nota:'))
media = (nota1 + nota2) / 2

if media >= 7:
    print('Aprovado')
else:
    nota3 = float(input('Digite sua terceira nota:'))
    media = (nota1 + nota2 + nota3 * 2) / 4
    if media >= 6:
        print('Aprovado')
    else:
        print('Reprovado')

print('-+-'*30)
print('Média do aluno: ', media)
print('-+-'*30)

