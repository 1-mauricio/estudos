# Considere um arquivo texto com nome externo  ́discip.old ́, contendo informações de disciplinas
# (Código com 5 posições, nome com 35 posições e créditos com 2 posições), uma disciplina por
# linha. Faça um programa Python para criar um segundo arquivo com nome externo  ́discip.new ́
# contendo informações das mesmas disciplinas, mas com as seguintes modificações:
#(a) As disciplinas cujos códigos são IF125 e IF380 devem ser excluídas, i.e., não devem ser
#gravadas no novo arquivo.
#(b) Os números de créditos das disciplinas cujos códigos começam por MA devem ser
#alterados para 5.
#(c) O novo arquivo terá um campo a mais (carga horária, com 3 posições) cujo valor deve ser
#o número de créditos da disciplina multiplicado por 15.
#No final o seu programa deve imprimir o número de disciplinas de cada arquivo e também o
#número de disciplinas que tiveram seus números de créditos alterados.

try:
    arq_leitura = open('Aulas\Slide 12 (Arquivos de Texto)\Fundamentos68\discip.old.txt', 'r')
    arq_escrita = open('Aulas\Slide 12 (Arquivos de Texto)\Fundamentos68\discp.new.txt', 'w')
    with arq_leitura, arq_escrita:
        for linha in arq_leitura:
            codigo = linha[0:5]
            nome_disc = linha[6:41]
            credito = linha[42:44]

            if (codigo != 'IF125') and (codigo != 'IF380'):
                if codigo[0:2] == 'MA':
                    credito = '5'
                carga = int(credito) * 15
                arq_escrita.write(f"{codigo} {nome_disc} {credito:2} {str(carga):3}\n")

except FileNotFoundError:
    print("Arquivo não encontrado") 
except PermissionError:
    print("Arquivo sem permissão") 
else:
    print("Programa finalizado com sucesso")