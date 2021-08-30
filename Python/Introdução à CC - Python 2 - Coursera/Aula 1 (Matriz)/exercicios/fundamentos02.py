def cria_matriz_1(num_linhas, num_colunas, valor):
    matriz = [] #lista vazia
    for i in range(num_linhas):
        #criar a linha i
        linha = [] #lista vazia
        for j in range(num_colunas):
            linha.append(valor)
        #adiciona linha à matriz
        matriz.append(linha)

def cria_matriz_2(num_linhas, num_colunas):
    matriz = [] #lista vazia
    for i in range(num_linhas):
        #criar a linha i
        linha = [] #lista vazia
        for j in range(num_colunas):
            valor = int(input(f"Digite o elemento [{i}][{j}]: "))
            linha.append(valor)
        #adiciona linha à matriz
        matriz.append(linha)
    
    return matriz

def le_matriz():
    linhas = int(input("número de linhas: "))
    colunas = int(input("número de colunas: "))
    print(cria_matriz_2(linhas, colunas))

le_matriz()