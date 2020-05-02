from lib.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        # exceção gerada quando arquivo ou diretório não existe.
        return False
    else:
        return True
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
     print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PRODUTOS CADASTRADOS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()
def cadastrar(arq, nome='desconhecido', quantidade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{quantidade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
