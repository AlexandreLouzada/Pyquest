"""
Certo aço é classificado de acordo com o resultado de três testes, que devem
verificar se o mesmo satisfaz às seguintes especificações:

a.	Teste 1- conteúdo de carbono abaixo de 7%;
b.	Teste 2- dureza Rokwell maior que 50;
c.	Teste 3- resistência à tração maior do que 80.000 psi.

Ao aço é atribuído o grau 10, se passa pelos três testes; 9 , se passa apenas
nos testes 1 e 2; 8 , se passa no teste 1; e 7, para as outras alternativas.

Supondo que sejam lidos de uma unidade de entrada o número de amostra,
conteúdo de carbono, a dureza Rokwell e a resistência à tração faça um programa
que leia os dados de uma amostra de aço, escrevendo para ela o grau obtido.
"""
print('**** Teste do aço ****')

amostra = int(input('Digite o número da amostra...:'))
carbono = float(input('Digite o conteúdo de carbono :'))
rokwell = float(input('Digite a dureza Rokwell......:'))
tração = float(input('Digite a resistência a tração:'))

print(f'Resultado do teste da amostra {amostra}:')

if carbono < 7 and rokwell > 50 and tração > 80.000:
    print('Grau 10')
elif carbono < 7 and rokwell > 50:
    print('Grau 9')
elif carbono < 7:
    print('Grau 8')
else:
    print('Grau 7')