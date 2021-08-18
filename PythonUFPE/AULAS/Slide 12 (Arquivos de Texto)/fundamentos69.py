# O arquivo “titanic.txt” disponibiliza informações dos passageiros que embarcaram no navio. Faça a
# leitura deste arquivo e, em seguida, armazene em um outro arquivo (“sobreviventes.txt”) o nome, o
# sexo e a idade dos passageiros que sobreviveram. Ao encerrar o programa, mostre na tela a
# quantidade de homens e mulheres sobreviventes bem como a média da idade deles (independente
# do sexo).
try:
    qtdHomens = 0
    qtdMulheres = 0
    media = 0
    qtd = 0
    arq_lido = open('Aulas\Slide 12 (Arquivos de Texto)\Fundamentos69\Titanic.txt','r')
    arq_escrita = open('Aulas\Slide 12 (Arquivos de Texto)\Fundamentos69\sobreviventes.txt', 'w')
    with arq_lido, arq_escrita:
        for linha in arq_lido:
            pessoa = linha.split(",")        
            sobrevivente = pessoa[1]
            nome = pessoa[3]
            sexo = pessoa[4]
            idade = pessoa[5]
            if sobrevivente == '1':
                qtd += 1
                if sexo == "male":
                    qtdHomens += 1
                else:
                    qtdMulheres += 1
                media += float(idade)
                arq_escrita.write(f"{nome} {sexo} {idade}\n")
    media /= (qtd)

except FileNotFoundError:
    print("Arquivo/caminho não foi encontrado")

except PermissionError:
    print("Arquivo sem permissão") 

except:
    print("Erro inesperado")

else: 
    print("O programa foi finalizado com sucesso.")
    print(f"A quantidade de homens sobreviventes foi de: {qtdHomens}")
    print(f"A quantidade de mulheres sobreviventes foi de: {qtdMulheres}")
    print(f"A média das idades foi de: {media}")