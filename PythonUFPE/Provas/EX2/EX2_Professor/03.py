def calculaCompra(estMinimo, estAtual):
    if estAtual < estMinimo * 0.5:
        qtd = 1.2 * estMinimo - estAtual
    elif estAtual <= estMinimo * 0.9:
        qtd = 1.1 * estMinimo - estAtual
    elif estAtual < estMinimo:
        qtd = estMinimo - estAtual
    else:
        qtd = 0
    return int(qtd)


fim = False
while not fim:
    try:
        nome_arq = input("Digite o nome/caminho do arquivo que será lido: ")
        arq_leitura = open(nome_arq, 'r')
        arq_escrita = open('compras.txt', 'w')
        with arq_leitura, arq_escrita:
            for linha in arq_leitura:
                codigo = linha[0:3]
                nome = linha[4:24]
                qtd_minima = int(linha[25:29])
                qtd_atual = int(linha[30:34])
                if qtd_atual < qtd_minima:
                    reposicao = calculaCompra(qtd_minima, qtd_atual)
                    arq_escrita.write(f'{codigo} {nome} {str(reposicao):4}\n')
    except FileNotFoundError:
       print("Erro. Nome/caminho do arquivo não encontrado.")
    else:
        print("Operações realizadas com sucesso.")
        fim = True
