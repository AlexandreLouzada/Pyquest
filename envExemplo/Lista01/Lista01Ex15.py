"""
Jogo de Pedra, papel e tesoura: nesse jogo cada jogador faz sua escolha
(1 –Tesoura, 2 – Pedra, 3 – Papel), e vence aquele que escolher um objeto
que seja capaz de vencer o outro:
•	Tesoura corta papel
•	Pedra quebra tesoura
•	Papel embrulha a pedra

Faça que leia a opção de objeto do primeiro jogador, a opção de objeto do segundo
 jogador e informe qual jogador venceu (ou se houve empate).
"""

escolha = """
==============================
1 - PEDRA ✊
2 - PAPEL ✋
3 - TESOURA ✌
==============================
{} ESCOLHE: """

j1_escolha = int(input(escolha.format('JOGADOR 1')))
j2_escolha = int(input(escolha.format('JOGADOR 2')))
print('='*30)

if (j1_escolha == 1) and (j2_escolha == 3):
    print('JOGADOR 1 ESMAGOU A TESOURA COM SUA PEDRA!!! ✊')
elif (j1_escolha == 3) and (j2_escolha == 2):
    print('JOGADOR 1 PICOTOU O PAPEL COM SUA TESOURA!!! ✌')
elif (j1_escolha == 2) and (j2_escolha == 1):
    print('JOGADOR 1 EMBRULHOU A PEDRA COM SEU PAPEL!!! ✋')
elif (j2_escolha == 1) and (j1_escolha == 3):
    print('JOGADOR 2 ESMAGOU A TESOURA COM SUA PEDRA!!! ✊')
elif (j2_escolha == 3) and (j1_escolha == 2):
    print('JOGADOR 2 PICOTOU O PAPEL COM SUA TESOURA!!! ✌')
elif (j2_escolha == 2) and (j1_escolha == 1):
    print('JOGADOR 2 EMBRULHOU A PEDRA COM SEU PAPEL!!! ✋')
else:
    print('HOUVE UM EMPATE!!! ')
