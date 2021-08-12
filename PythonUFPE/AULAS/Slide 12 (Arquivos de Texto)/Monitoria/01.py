# formato das linhas: nº cadastro sexo pontos nome
# mostrar: 1. quem tem a maior pontuação; 2. quem tem a menor pontuação; 3. quantidade de homens; 4. quantidade de mulheres 
try:
    arquivo = open("Aulas\Slide 12(Arquivos de Texto)\Monitoria\exercicio-monitoria.txt", "r")
    
    maiorPontuacao = [-999999999, ""]
    menorPontuacao = [9999999999, ""]

    qtdHomens = 0
    qtdMulheres = 0

    numMedia = 0
    denMedia = 0

    for linha in arquivo:
        cadastro = linha[0:5]
        sexo = linha[6:7]
        pontuacao = int(linha[8:15])
        nome = linha[16:50].strip()

        numMedia += pontuacao
        denMedia += 1

        if pontuacao > maiorPontuacao[0]:
            maiorPontuacao[0] = pontuacao
            maiorPontuacao[1] = nome

        if pontuacao < menorPontuacao[0]:
            menorPontuacao[0] = pontuacao
            menorPontuacao[1] = nome

        if sexo == '1':
            qtdHomens += 1
        else:
            qtdMulheres += 1

    arquivo.close()

except:
    print('deu erro')

print(f'Maior Pontuação: {maiorPontuacao[1]} com {maiorPontuacao[0]} pontos.')
print(f'Menor Pontuação: {menorPontuacao[1]} com {menorPontuacao[0]} pontos.')

print(f'Quantidade homens: {qtdHomens}')
print(f'Quantidade mulheres: {qtdMulheres}')