def MelhoresClientes(nome, pont_refer):
    cont_total = 0
    cont_melhores = 0
    media = 0
    arq = open(f"Provas\Provas antigas\EX2\\2020.1\{nome}.txt", 'r')
    arq_esc = open(f'Provas\Provas antigas\EX2\\2020.1\{nome}Melhores.txt', 'w')
    with arq, arq_esc:
        for linha in arq:
            cont_total+= 1
            matricula = linha[0:5]
            sexo = linha[6:7]
            pontos = int(linha[8:15])
            nome_c = linha[16:51]
            if pontos > pont_refer:
                arq_esc.write(f'{matricula} {pontos}\n')
                cont_melhores += 1
                media += pontos
    media /= cont_melhores

    print(f'Nome da empresa: {nome} \nNúmero de registros: {cont_total} \nMédia da pontuação: {media}')

fim = False
N = int(input("Digite a quantidade de empresas a ser lido: "))
while not fim:
    try:
        nome = input("Digite o nome da empresa: ")
        pont = int(input("Digite o total de pontos referência: "))
        MelhoresClientes(nome, pont)

    except FileNotFoundError:
        print("Nome/caminho de arquivo inválido.")    
    
    else:
        N -= 1
        if N == 0:
            print("O programa foi finalizado com sucesso.")
            fim = True