"""
Tendo como dados de entrada a altura e o sexo de uma pessoa
(M - masculino e F - feminino), construa um algoritmo que calcule
seu peso ideal, utilizando as seguintes fórmulas:
- para homens: (72.7*h)-58
- para mulheres: (62.1*h)-44.7
"""
sexo= input("Digite seu sexo (m) para masculino e (f) para feminino:")
h= float(input('Digite sua altura:'))
sexo = sexo.upper()
if sexo == 'M':
    pesoideal= (72.7*h)-58
elif sexo =='F':
    pesoideal= (62.1*h)-44.7
print('seu peso ideal é de {:.2f} kg'.format(pesoideal))
