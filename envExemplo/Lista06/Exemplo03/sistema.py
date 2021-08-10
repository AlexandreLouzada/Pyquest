from lib.interface import *
from lib.arquivo import *
from time import sleep
arq = 'exemploarquivo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Listar produto', 'Cadastrar produto', 'Sair'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar um novo produto.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        quantidade = leiaInt('Quantidade: ')
        cadastrar(arq, nome, quantidade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no menu.
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
