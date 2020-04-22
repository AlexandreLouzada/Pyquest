nome = input('Digite o nome: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda  nota: '))
média = (nota1+nota2)/2
if média >= 7:
    situação = 'Aprovado'
else:
    situação = 'Reprovado'
print(f'O aluno(a) {nome} obteve a média {média} - Situação: {situação}')
