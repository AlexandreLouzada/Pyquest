from conversor import converter_moeda
from cotacoes import obter_cotacao_moedas

def exibir_menu():
    print("1. Converter de Real para Dólar")
    print("2. Converter de Real para Euro")
    print("3. Converter de Real para Libra")
    print("4. Sair")

# Obtém as cotações de moedas
cotacoes = obter_cotacao_moedas()

if cotacoes:
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            valor = float(input("Digite o valor em Real (BRL): "))
            valor_convertido = converter_moeda(valor, "BRL", "USD", cotacoes)
            if valor_convertido:
                print(f"Valor convertido: {valor_convertido} USD")
            else:
                print("Não foi possível realizar a conversão.")
        
        elif opcao == "2":
            valor = float(input("Digite o valor em Real (BRL): "))
            valor_convertido = converter_moeda(valor, "BRL", "EUR", cotacoes)
            if valor_convertido:
                print(f"Valor convertido: {valor_convertido} EUR")
            else:
                print("Não foi possível realizar a conversão.")

        elif opcao == "3":
            valor = float(input("Digite o valor em Real (BRL): "))
            valor_convertido = converter_moeda(valor, "BRL", "GBP", cotacoes)
            if valor_convertido:
                print(f"Valor convertido: {valor_convertido} GBP")
            else:
                print("Não foi possível realizar a conversão.")
        
        elif opcao == "4":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Digite novamente.")
else:
    print("Não foi possível obter as cotações de moedas. Encerrando o programa.")

