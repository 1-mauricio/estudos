import funcao

fim = False

while not fim:
    dias_usuario = int(input("Digite a quantidade de dias (0 encerra): "))
    if dias_usuario == 0:
        fim = True

    seculos = 0
    decadas = 0
    anos = 0
    meses = 0
    semanas = 0
    dias = dias_usuario

    seculos = funcao.contagem(dias, seculos, 36500)
    dias = seculos[1]
    decadas = funcao.contagem(dias, decadas, 3650)
    dias = decadas[1]
    anos = funcao.contagem(dias, anos, 365)
    dias = anos[1]
    meses = funcao.contagem(dias, meses, 30)
    dias = meses[1]
    semanas = funcao.contagem(dias, semanas, 7)
    dias = semanas[1]
    dias = funcao.contagem(dias, dias, 1)

    print(f"{dias_usuario} dias equivalem a: \n{seculos[0]} séculos, \n{decadas[0]} decadas, \n{anos[0]} ano(s), \n{meses[0]} mes(es), \n{semanas[0]} semanas e \n{dias[0]} dia(s)")