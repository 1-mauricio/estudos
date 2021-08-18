def calculaCompra(qtdMinima, qtdAtual):
    if qtdAtual < qtdMinima/2:
        qtdMinima = qtdMinima*1.2 
        qtdCompra = qtdMinima - qtdAtual

    elif qtdAtual > qtdMinima/2 and qtdAtual < qtdMinima*0.9:
        qtdMinima = qtdMinima*1.1 
        qtdCompra = qtdMinima - qtdAtual

    elif qtdAtual > qtdMinima*0.9: 
        qtdCompra = qtdMinima - qtdAtual

    return qtdCompra

try:
    nome = input("Digite o nome do arquivo a ser lido: ")
    if ".txt" not in nome:
        nome += ".txt"
    arq_lido = open(nome, 'r')
    arq_escrito = open('compras.txt', 'w')
    with arq_lido, arq_escrito: 
        for linha in arq_lido:
            codigo = int(linha[0:3])
            nome = linha[4:24].strip()
            qtdMinima = int(linha[25:29])
            qtdAtual = int(linha[30:34])
            if qtdMinima>qtdAtual:
                qtdCompra = calculaCompra(qtdMinima, qtdAtual)              
                arq_escrito.write(f"{codigo} {nome} {qtdCompra:.0f}\n")

except FileNotFoundError:
    print("Arquivo/caminho não encontrado")

except PermissionError:
    print("O programa não tem permissão para acessar o arquivo")

except:
    print("Erro não previsto")

else:
    print('o programa foi finalizado com sucesso')