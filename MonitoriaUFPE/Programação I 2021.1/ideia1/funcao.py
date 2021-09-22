def contagem (dias, nome, qtd, aux=0):
    dias -= aux
    while dias >= qtd:
        nome += 1
        dias -= qtd

    return nome, dias