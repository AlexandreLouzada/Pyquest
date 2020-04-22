equipe = input('Digite o nome da equipe: ')
vitórias = int(input('Digite a quantidade de vitórias:'))
empates = int(input('Digite a quantidade de  empates:'))
derrotas = int(input('Digite a quantidade de derrotas:'))
pontos_ganhos = vitórias * 3 + empates
pontos_perdidos = derrotas * 3 + derrotas * 2
total_jogos = vitórias + derrotas + empates
print('-=' * 40)
print(f'A equipe {equipe} disputou {total_jogos} jogos com o seguinte desempenho:')
print(f'{pontos_ganhos} pontos ganhos e {pontos_perdidos} pontos perdidos')
print('-=' * 40)
