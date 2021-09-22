def contagem (dias, nome, qtd, aux=0):
    dias -= aux
    while dias >= qtd:
        nome += 1
        dias -= qtd

    return nome, dias

dias_usuario = int(input("Digite a quantidade de dias: "))

anos = 0
meses = 0
dias = dias_usuario

anos = contagem(dias, anos, 365)
dias = anos[1]
meses = contagem(dias, meses, 30)
dias = meses[1]
dias = contagem(dias, dias, 1)

print(f"{dias_usuario} dias equivalem a {anos[0]} ano(s), {meses[0]} mes(es) e {dias[0]} dia(s)")