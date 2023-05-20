def obter_nome_moeda(sigla):
    nome_moedas = {
        "USD": "Dólar Americano",
        "EUR": "Euro",
        "GBP": "Libra Esterlina",
        "JPY": "Iene Japonês",
        "CAD": "Dólar Canadense",
    }
    return nome_moedas.get(sigla, sigla)
