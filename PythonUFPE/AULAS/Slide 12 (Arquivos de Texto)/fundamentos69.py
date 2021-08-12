# O arquivo “titanic.txt” disponibiliza informações dos passageiros que embarcaram no navio. Faça a
# leitura deste arquivo e, em seguida, armazene em um outro arquivo (“sobreviventes.txt”) o nome, o
# sexo e a idade dos passageiros que sobreviveram. Ao encerrar o programa, mostre na tela a
# quantidade de homens e mulheres sobreviventes bem como a média da idade deles (independente
# do sexo).

    
try:
    pessoa = []
    arq_lido = open(f'Aulas\Slide 12 (Arquivos de Texto)\Fundamentos69\titanic.txt','r')
    with arq_lido:
        for linha in arq_lido:
            pessoa[:] = linha.split()
except FileNotFoundError:
    print(f"Arquivo/caminho {nome} não encontrado")



matricula, sexo, pontos, nome_c = linha.split()