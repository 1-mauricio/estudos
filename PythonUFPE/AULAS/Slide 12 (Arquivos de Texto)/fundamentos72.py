try:
    arq_lido = open(f'Aulas\Slide 12 (Arquivos de Texto)\Fundamentos67\profissoes.txt','r')
    arq_escrito = open(f'Aulas\Slide 12 (Arquivos de Texto)\Fundamentos67\cod_invalidos1.txt', 'w')
    dic = {}
    with arq_lido:
        for linha in arq_lido:
            cod = int(linha[0:3])
            nome = linha[4:34].strip()
            dic[cod] = nome

    fim = False    
    while not fim:
        try:
            codigo = int(input('Digite um código positivo (zero ou negativo p/ encerrar): '))
            with arq_escrito:
                while codigo > 0:
                    if codigo in dic:
                        print(f"O código {codigo} corresponde à profissão de {dic[codigo]}")
                    else:    
                        print("Profissão inexistente")
                        arq_escrito.write(f'{codigo}\n')
                    codigo = int(input('Digite um código positivo (zero ou negativo p/ encerrar): '))

        except FileNotFoundError:
            print("Arquivo/caminho não encontrado")

        except PermissionError:
            print("Erro de permissão")
        
        except ValueError:
            print("O número deve ser inteiro.")

        else:
            fim = True

except FileNotFoundError:
    print("Arquivo/caminho não encontrado")

except PermissionError:
    print("Erro de permissão")

except:
    print("Erro inesperado")

else:
    print("O programa foi finalizado com sucesso")