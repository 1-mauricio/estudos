def ler_arquivo(nome='profissoes.txt'):
    dict = {}
    try:
        arq_lido = open(f'Aulas\Slide 12 (Arquivos de Texto)\Fundamentos67\{nome}','r')
        with open(f'Aulas\Slide 12 (Arquivos de Texto)\Fundamentos67\{nome}','r') as arq_lido:
            for linha in arq_lido:
                lst = linha.split()
                dict[int(lst[0])] = ' '.join(lst[1:])
    except FileNotFoundError:
        print(f"Arquivo/caminho {nome} não encontrado")

    return dict

dict = ler_arquivo()
fim = False
while not fim:
    try: 
        codigo = int(input('Digite um código positivo (zero ou negativo p/ encerrar): '))
        while codigo > 0:
            if codigo in dict:
                print(f"O código {codigo} corresponde à profissão de {dict[codigo]}")
            else:
                print("Profissão inexistente")
                with open('Aulas\Slide 12 (Arquivos de Texto)\Fundamentos67\cod_invalidos.txt', 'a') as arq_invalido:
                    arq_invalido.write(f'{codigo}\n')

            codigo = int(input('Digite um código positivo (zero ou negativo p/ encerrar): '))
    except ValueError:
        print("O código deve ser um número inteiro.")
    except PermissionError:
        print("Sem permissão de criação de arquivo.")
    else:
        fim = True