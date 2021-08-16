# (a) ler um arquivo (nome externo 'clientes.arq'), contendo informações das pessoas que são
# clientes do programa de fidelidade da empresa: matric (inteiro com 5 dígitos), sexo (1=masc.
# ou 2=fem.), pontos (inteiro com 7 dígitos), e nome (string com 35 posições).
# (b) criar um arquivo (nome externo 'melhores.arq') contendo somente a matrícula e o total de
# pontos (um cliente por linha) com pontuação acima de um dado valor (informado antes pelo
# usuário).
# (c) No final, o programa deve imprimir (na tela do terminal) um resumo das informações
# gravadas no arquivo contendo o número de registros gravados no arquivo e a média das
# pontuações destes clientes.

try:
    arquivo_lido = open('Provas\Provas antigas\EX2\\2015.2\clientes.arq', 'r')
    arquivo_escrito = open('Provas\Provas antigas\EX2\\2015.2\melhores.arq', 'w')
    valor = int(input("Digite o valor referencia: "))
    qtdRegistros = 0
    media = 0
    with arquivo_lido, arquivo_escrito:
        for linha in arquivo_lido:
            matric = linha[0:5]
            sexo = linha[6:7]
            pontos = int(linha[8:15])
            nome = linha[16:51]
            if pontos > valor:
                media += pontos
                qtdRegistros += 1
                arquivo_escrito.write(f"{matric} {pontos}\n")
    media /= qtdRegistros

except FileNotFoundError:
    print('O arquivo/caminho não foi encontrado')

except PermissionError:
    print("Arquivo sem permissão")

except:
    print("Erro inesperado.")

else:
    print("Programa foi executado com sucesso")
    print(f"{qtdRegistros} registros foram gravados no arquivo")
    print(f"A média dos registros foi de: {media}")
