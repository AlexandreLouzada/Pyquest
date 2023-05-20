def converter_moeda(valor, moeda_origem, moeda_destino, cotacoes):
    if cotacoes:
        if moeda_origem == "BRL":
            valor_origem = valor
        else:
            valor_origem = valor / cotacoes[moeda_origem]

        if moeda_destino == "BRL":
            valor_convertido = valor_origem
        else:
            valor_convertido = valor_origem * cotacoes[moeda_destino]

        return valor_convertido
    else:
        return None

