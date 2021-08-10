def MelhoresClientes(nome, pont_refer):
    nome += '.txt'
    cont_total = 0
    cont_melhores = 0
    media = 0
    arq = open(nome, 'r')
    arq_esc = open(f'{nome}Melhores.txt', 'w')
    with arq, arq_esc:
        for linha in arq:
            cont_total+= 1
            matricula, sexo, pontos, nome_c = linha.split()
            if int(pontos) > pont_refer:
                arq_esc.write(f'{matricula} {pontos}\n')
                cont_melhores += 1
                media += pontos
    media /= cont_melhores

    print(f'Nome da empresa: {nome} \nNúmero de registros: {cont_total} \nMédia da pontuação: {media}')

fim = False
while not fim:
    try:
        nome = input("Digite o nome da empresa: ")
        pont = int(input("Digite o total de pontos referência: "))
        MelhoresClientes(nome, pont)

    except FileNotFoundError:
        print("Nome/caminho de arquivo inválido.")    
    
    else:
        print("O programa foi finalizado com sucesso.")
        fim = True