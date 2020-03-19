"""
Construir um programa leia um número inteiro entre 1 e 7 e imprima o nome do dia
da semana correspondente ao número, caso o número esteja fora do intervalo entre
1 e 7, imprimir “Dia Inválido”.
"""
semana= int(input('digite um numero:'))
if semana == 1:
    print('domingo')
elif semana == 2:
    print('segunda')
elif semana == 3:
    print('terça')
elif semana == 4:
    print('quarta')
elif semana == 5:
    print('quinta')
elif semana == 6:
    print('sexta')
elif semana == 7:
    print('sabado')
else:
    print('Dia invalido')
