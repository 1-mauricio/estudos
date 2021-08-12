fim = False
cont = 0
while not fim:
    try:
        nome = input("Digite o nome do arquivo: ")
        arq = open(nome, 'r')
        arq_esc = open('Aulas\Slide 12(Arquivos de Texto)\fundamentos66\veicVelhos.txt', 'w')

        with arq, arq_esc:
            for linha in arq:
                placa, marca, modelo, ano, cpf = linha.split()
                if int(ano) <= 2000:
                    arq_esc.write(f"{placa} {ano} {cpf}\n")
                    cont += 1
# NÃO NECESSÁRIO      arq.close()
# COM O WITH          arq_esc.close()
    except FileNotFoundError:
        print("Nome/caminho de arquivo inválido.")
    else:
        print("O programa foi finalizado com sucesso.")
        print(f"Número de veículos velhos gravados no arquivo: {cont}")
        fim = True

    